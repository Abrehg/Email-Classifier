from CreateService import gmailServiceCreate
from CreateService import Inter, Promo, College
import pandas as pd
from text_parsing import normalize_text
import gensim
import gensim.corpora as corpora
import os

service = gmailServiceCreate()

college = "Label_2759360573854140636"
interpersonal = "Label_267554376139622606"
promotional = "Label_4549946469515729599"

def search_inbox(service):
    result = service.users().messages().list(userId='me', maxResults=8000).execute()
    messages = [ ]
    if 'messages' in result:
        messages.extend(result['messages'])
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me', maxResults=8000, pageToken=page_token).execute()
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages

def search_messages(service, label):
    result = service.users().messages().list(userId='me',labelIds=label, maxResults=8000).execute()
    messages = [ ]
    if 'messages' in result:
        messages.extend(result['messages'])
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me',labelIds=label, maxResults=8000, pageToken=page_token).execute()
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages

def read_message(service, message):
    msg = service.users().messages().get(userId='me', id=message, format='full').execute()
    # parts can be the message body, or attachments
    payload = msg['payload']
    return(payload)

def get_snippet(service, message):
    msg = service.users().messages().get(userId='me', id=message, format='full').execute()
    # parts can be the message body, or attachments
    snippet = msg['snippet']
    return(snippet)

TotResult = search_inbox(service)
all = 0
AllId = [["Id"],["sender"],["subject"],["subject topic"],["body"],["body topic"],["has_emoji"],["label"]]
while all < len(TotResult):
    AllId[0].append(TotResult[all]['id'])
    AllId[1].append("fill")
    AllId[2].append("fill")
    AllId[3].append(0)
    AllId[4].append("fill")
    AllId[5].append(0)
    AllId[6].append(0)
    AllId[7].append(0)
    all = all + 1
print("AllId created")

SentResult = search_messages(service, "SENT")
sent = 0
SentId = ["Inter"]
while sent < len(SentResult):
    SentId.append(SentResult[sent]['id'])
    sent = sent + 1
SentId.pop(0)
print("SentId created")

InterResult = search_messages(service, Inter)
inter = 0
InterId = ["Inter"]
while inter < len(InterResult):
    InterId.append(InterResult[inter]['id'])
    inter = inter + 1
InterId.pop(0)
print("InterId created")

CollegeResult = search_messages(service, College)
college = 0
CollegeId = ["college"]
while college < len(CollegeResult):
    CollegeId.append(CollegeResult[college]['id'])
    college = college + 1
CollegeId.pop(0)
print("CollegeId created")

PromoResult = search_messages(service, Promo)
promo = 0
PromoId = ["Promo"]
while promo < len(PromoResult):
    PromoId.append(PromoResult[promo]['id'])
    promo = promo + 1
PromoId.pop(0)
print("PromoId created")

counter = 1
ct = 0
AllIdInstance = ""
SentIdInstance = ""
result = ""
iterations = 0
while counter < len(AllId[0]):
    AllIdInstance = str(AllId[0][counter])
    while ct < len(SentId):
       SentIdInstance = str(SentId[ct])
       if SentIdInstance == AllIdInstance:
          SentId.pop(ct)
          AllId[0].pop(counter)
          AllId[1].pop(counter)
          AllId[2].pop(counter)
          AllId[3].pop(counter)
          AllId[4].pop(counter)
          AllId[5].pop(counter)
          AllId[6].pop(counter)
          AllId[7].pop(counter)
       ct = ct + 1
       iterations = iterations + 1
    counter = counter + 1
    ct = 0
counter = 1
while counter < len(AllId[0]):
    AllIdInstance = str(AllId[0][counter])
    while ct < len(SentId):
       SentIdInstance = str(SentId[ct])
       if SentIdInstance == AllIdInstance:
          SentId.pop(ct)
          AllId[0].pop(counter)
          AllId[1].pop(counter)
          AllId[2].pop(counter)
          AllId[3].pop(counter)
          AllId[4].pop(counter)
          AllId[5].pop(counter)
          AllId[6].pop(counter)
          AllId[7].pop(counter)
       ct = ct + 1
       iterations = iterations + 1
    counter = counter + 1
    ct = 0
counter = 1
while counter < len(AllId[0]):
    AllIdInstance = str(AllId[0][counter])
    while ct < len(SentId):
       SentIdInstance = str(SentId[ct])
       if SentIdInstance == AllIdInstance:
          SentId.pop(ct)
          AllId[0].pop(counter)
          AllId[1].pop(counter)
          AllId[2].pop(counter)
          AllId[3].pop(counter)
          AllId[4].pop(counter)
          AllId[5].pop(counter)
          AllId[6].pop(counter)
          AllId[7].pop(counter)
       ct = ct + 1
       iterations = iterations + 1
    counter = counter + 1
    ct = 0
counter = 1
while counter < len(AllId[0]):
    AllIdInstance = str(AllId[0][counter])
    while ct < len(SentId):
       SentIdInstance = str(SentId[ct])
       if SentIdInstance == AllIdInstance:
          SentId.pop(ct)
          AllId[0].pop(counter)
          AllId[1].pop(counter)
          AllId[2].pop(counter)
          AllId[3].pop(counter)
          AllId[4].pop(counter)
          AllId[5].pop(counter)
          AllId[6].pop(counter)
          AllId[7].pop(counter)
       ct = ct + 1
       iterations = iterations + 1
    counter = counter + 1
    ct = 0
counter = 1
while counter < len(AllId[0]):
    AllIdInstance = str(AllId[0][counter])
    while ct < len(SentId):
       SentIdInstance = str(SentId[ct])
       if SentIdInstance == AllIdInstance:
          SentId.pop(ct)
          AllId[0].pop(counter)
          AllId[1].pop(counter)
          AllId[2].pop(counter)
          AllId[3].pop(counter)
          AllId[4].pop(counter)
          AllId[5].pop(counter)
          AllId[6].pop(counter)
          AllId[7].pop(counter)
       ct = ct + 1
       iterations = iterations + 1
    counter = counter + 1
    ct = 0
print("SentId Ids removed")

ctr = 1
while ctr < len(AllId[0]):
    a = 0
    b = 0
    c = 0
    while a < len(InterId):
        if AllId[0][ctr] == InterId[a]:
            AllId[7][ctr] = 1
            InterId.pop(a)
        a = a + 1
    while b < len(CollegeId):
        if AllId[0][ctr] == CollegeId[b]:
            AllId[7][ctr] = 3
            CollegeId.pop(b)
        b = b + 1
    while c < len(PromoId):
        if AllId[0][ctr] == PromoId[c]:
            AllId[7][ctr] = 2
            PromoId.pop(c)
        c = c + 1
    ctr = ctr + 1
print("AllId classified")

i = 1
h = 0

while i < len(AllId[0]):
    message = read_message(service, AllId[0][i])
    while h < len(message["headers"]):
        if message["headers"][h]['name'] == 'From':
            AllId[1][i] = message["headers"][h]['value']
        if message["headers"][h]['name'] == 'Subject':
            AllId[2][i] = message["headers"][h]['value']
        h = h + 1
    h = 0
    i = i + 1

print("Subject and Sender Info added")

j = 1

while j < len(AllId[0]):
    snippet = get_snippet(service, AllId[0][j])
    AllId[4][j] = snippet
    j = j + 1

print("Snippet added")

file_exists = os.path.exists("Sender.csv")
if file_exists == True:
    sender = pd.read_csv("Sender.csv", header=None)

    i = 0
    while i < len(AllId[1]):
       maximum = 0
       while maximum < len(sender):
           if AllId[1][i] == sender.iat[maximum, 0]:
               AllId[1][i] = maximum
           maximum = maximum + 1
       if type(AllId[1][i]) == str:
           newSender = pd.DataFrame([AllId[1][i]])
           sender.append(newSender, ignore_index=True)
           AllId[1][i] = maximum
       i = i + 1
    os.remove("Sender.csv")
    sender.to_csv("Sender.csv", index=False, header=False)
elif file_exists == False:
    sender = []
    i = 0
    while i < len(AllId[1]):
      maximum = 0
      while maximum < len(sender):
          if AllId[1][i] == sender[maximum]:
              AllId[1][i] = maximum
          maximum = maximum + 1
      if type(AllId[1][i]) == str:
          sender.append(AllId[1][i])
          AllId[1][i] = maximum
      i = i + 1
    data = pd.DataFrame(data = sender)
    data.to_csv("Sender.csv", index=False)

print("Sender info converted to numerical form")

count = 1

while count < len(AllId[0]):
    AllId[2][count], AllId[5][count] = normalize_text(AllId[2][count])
    AllId[4][count], AllId[5][count] = normalize_text(AllId[4][count])
    count = count + 1
print("Text normalized")

i = 0

while i < len(AllId):
    AllId[i].pop(0)
    i = i + 1
print("labels removed")

# Loading in lda models for subject and body
lda = gensim.models.LdaModel.load("LDAModel.pickle")
print("LDA models loaded")

# using LDA to find topic of subject
Dictionary = corpora.Dictionary(AllId[2])
texts = AllId[2]
corpus = [Dictionary.doc2bow(text) for text in texts]
i = 0
while i < len(AllId[2]):
    max = 0.0
    max_index = 0
    results = 0
    result = lda[corpus[i]]
    while results < len(result):
        if result[results][1] > max:
            max = result[results][1]
            max_index = result[results][0]
        results = results + 1
    AllId[3][i] = max_index
    i = i + 1
print("AllId[3] updated")

# using LDA to find topic of body
Dictionary = corpora.Dictionary(AllId[4])
texts = AllId[4]
corpus = [Dictionary.doc2bow(text) for text in texts]
i = 0
while i < len(AllId[4]):
    max = 0.0
    max_index = 0
    results = 0
    result = lda[corpus[i]]
    while results < len(result):
        if result[results][1] > max:
            max = result[results][1]
            max_index = result[results][0]
        results = results + 1
    AllId[5][i] = max_index
    i = i + 1
print("AllId[5] updated")

data = pd.DataFrame(AllId)
data = data.T
data = data.rename(columns = {
    0 : "Id",
    1 : "Sender",
    2 : "Subject",
    3 : "Subject Topic",
    4 : "Body",
    5 : "Body Topic",
    6 : "Has_Emoji",
    7 : "Class"})
print("dataset created")

print(data)

os.remove("Model_Data.csv")
data.to_csv("Model_Data.csv")
