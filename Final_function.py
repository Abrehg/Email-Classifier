import pickle
from text_parsing import normalize_text
from CreateService import gmailServiceCreate
from CreateService import College, Inter, Promo
import gensim
import gensim.corpora as corpora
import pandas as pd
import os
from datetime import datetime

service = gmailServiceCreate()

def current_time():
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")
   print(current_time)

def search_inbox(service):
    result = service.users().messages().list(userId='me', maxResults=1).execute()
    messages = [ ]
    if 'messages' in result:
        messages.extend(result['messages'])
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me', maxResults=20000, pageToken=page_token).execute()
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages

def get_snippet(service, message):
    msg = service.users().messages().get(userId='me', id=message, format='full').execute()
    # parts can be the message body, or attachments
    snippet = msg['snippet']
    return(snippet)

def read_message(service, message):
    msg = service.users().messages().get(userId='me', id=message, format='full').execute()
    # parts can be the message body, or attachments
    payload = msg['payload']
    return(payload)

def trash_message(service, message_id):
    try:
        message = (service.users().messages().trash(userId='me', id=message_id).execute())
        print('Message Id: %s sent to Trash.' % message['id'])
        return message
    except Exception as error:
        print('An error occurred while sending email: %s' % error)
        return None

def remove_label(service, message_id, label_Id):
    post_data = {"removeLabelIds": [label_Id]}
    result = service.users().messages().modify(userId='me', id=message_id, body=post_data).execute()

def add_label(service, message_id, label_Id):
    post_data = {"addLabelIds": [label_Id]}
    result = service.users().messages().modify(userId='me', id=message_id, body=post_data).execute()

lda = gensim.models.LdaModel.load("LDAModel.pickle")

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
print("models loaded")
"""
Possible Labels: 
0 = Normal
1 = Interpersonal
2 = Promotional
3 = College

AllId parts:
0 : Id,
1 : Sender,
2 : Subject,
3 : Subject Topic,
4 : Body,
5 : Body Topic,
6 : Has_Emoji
"""

def Main_Function():
  current_time()
  email = [0, "Fill", "Fill", 0, "Fill", 0, 0]

  id_result = search_inbox(service)
  email[0] = id_result[0]["id"]
  print("Id retrieved")

  h = 0
  message = read_message(service, email[0])
  print("message read")
  while h < len(message["headers"]):
      if message["headers"][h]['name'] == 'From':
          email[1] = message["headers"][h]['value']
      if message["headers"][h]['name'] == 'Subject':
          email[2] = message["headers"][h]['value']
      h = h + 1
  print("Subject + sender received")

  snippet = get_snippet(service, email[0])
  email[4] = snippet
  print("body recieved")

  file_exists = os.path.exists("Sender.csv")
  if file_exists == True:
      sender = pd.read_csv("Sender.csv", header=None)

      maximum = 0
      while maximum < len(sender):
          if email[1] == sender.iat[maximum, 0]:
              email[1] = maximum
          maximum = maximum + 1
      if type(email[1]) == str:
          newSender = pd.DataFrame([email[1]])
          sender.append(newSender, ignore_index=True)
          email[1] = maximum
      os.remove("Sender.csv")
      sender.to_csv("Sender.csv", index=False, header=False)

  elif file_exists == False:
      sender = []
      maximum = 0
      while maximum < len(sender):
         if email[1] == sender[maximum]:
            email[1] = maximum
         maximum = maximum + 1
      if type(email[1]) == str:
         sender.append(email[1])
         email[1] = maximum

      data = pd.DataFrame(data=sender)
      data.to_csv("Sender.csv", index=False)

  email[2], email[5] = normalize_text(email[2])
  email[4], email[5] = normalize_text(email[4])
  print("text normalized")

  input = [[0],["test"]]
  input[0] = email[2]

  Dictionary = corpora.Dictionary(input)
  texts = input
  corpus = [Dictionary.doc2bow(text) for text in texts]
  max = 0.0
  max_index = 0
  results = 0
  result = lda[corpus[0]]
  while results < len(result):
      if result[results][1] > max:
          max = result[results][1]
          max_index = result[results][0]
      results = results + 1
  email[3] = max_index
  print("subject topic extracted")

  input = [[0], ["test"]]
  input[0] = email[4]

  Dictionary = corpora.Dictionary(input)
  texts = input
  corpus = [Dictionary.doc2bow(text) for text in texts]
  max = 0.0
  max_index = 0
  results = 0
  result = lda[corpus[0]]
  while results < len(result):
      if result[results][1] > max:
          max = result[results][1]
          max_index = result[results][0]
      results = results + 1
  email[5] = max_index
  print("body topic extracted")

  i = 0
  while i < len(email):
      print(f"{i} -- {email[i]}")
      i = i + 1

  id = email[0]

  email.pop(0)
  email.pop(1)
  email.pop(2)
  print("")
  i = 0
  while i < len(email):
      print(f"{i} -- {email[i]}")
      i = i + 1
  print("original text removed")
  print(email)

  feature = [[0, 0, 0, 0], [0, 0, 0, 0]]

  feature[0] = email
  print("features loaded")

  result = loaded_model.predict(feature)
  print("ran through model")
  print(f"predicted class: {result[0]}")

  classification = result[0]

  if classification == 1:
      add_label(service, id, Inter)
      trash_message(service, id)

  elif classification== 2:
      add_label(service, id, Promo)
      trash_message(service, id)

  elif classification == 3:
      add_label(service, id, College)
      remove_label(service, id, "INBOX")

  current_time()
  return None
