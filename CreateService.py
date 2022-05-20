from Google import create_service

def gmailServiceCreate():
    CLIENT_FILE = """Enter client ID here"""
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
    return service