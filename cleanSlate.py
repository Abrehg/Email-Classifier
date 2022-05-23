from CreateService import gmailServiceCreate
from CreateService import Inter, Promo, College

service = gmailServiceCreate()

def search_messages(service, label):
    result = service.users().messages().list(userId='me',labelIds=label, maxResults=20000).execute()
    messages = [ ]
    if 'messages' in result:
        messages.extend(result['messages'])
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me',labelIds=label, maxResults=20000, pageToken=page_token).execute()
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages

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

Inbox = "INBOX"

Inter_Result = search_messages(service, Inter)
j = 0
Inter_Id = []
while j < len(Inter_Result):
    Inter_Id.append(Inter_Result[j]["id"])
    j = j + 1

for id in Inter_Id:
    trash_message(service, id)

Promo_Result = search_messages(service, Promo)
j = 0
Promo_Id = []
while j < len(Promo_Result):
    Promo_Id.append(Promo_Result[j]["id"])
    j = j + 1

for id in Promo_Id:
    trash_message(service, id)

College_Result = search_messages(service, College)
j = 0
College_Id = []
while j < len(College_Result):
    College_Id.append(College_Result[j]["id"])
    j = j + 1

for id in College_Id:
    remove_label(service, id, Inbox)
