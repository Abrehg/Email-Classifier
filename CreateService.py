from Google import create_service

def gmailServiceCreate():
    CLIENT_FILE = 'client.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
    return service

Inter = "Label_267554376139622606"
Promo = "Label_4549946469515729599"
College = "Label_2759360573854140636"
Inbox = "INBOX"
