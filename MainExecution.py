import os
from cloud import pubsub_v1
from concurrent.futures import TimeoutError
from Final_function import Main_Function
from CreateService import gmailServiceCreate
from datetime import datetime
import threading
from modifyTokenFiles import replaceTokenFiles

service = gmailServiceCreate()

def current_time():
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")
   print(current_time)

def search_new_message():
  request = {
    'labelIds': ['INBOX'],
    'topicName': 'projects/valid-flow-336221/topics/notification_recieving_topic'
  }
  output = service.users().watch(userId='me', body=request).execute()

# This function gets called by our thread.. so it basically becomes the thread init...
def wait_for_event(e):
    while True:
        print("Starting the main function")
        event_is_set = e.wait()
        try:
            Main_Function()
        except __:
            os.remove("token files")
            replaceTokenFiles()
            Main_Function()
        except Exception:
            print(Exception)
            Main_Function()
        e.clear()

current_time()

now = datetime.now()
time_now = now.strftime("%H")

if time_now == "09":
  search_new_message()

search_new_message()

credentials_path = "credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

subscriber = pubsub_v1.SubscriberClient()
subscription_path = "projects/valid-flow-336221/subscriptions/notification_recieving_topic-sub"

e = threading.Event()
t = threading.Thread(name='pausable_thread',
                     target=wait_for_event,
                     args=(e,))

def callback(message):
    print(f"Received message: {message}")
    print(f"data: {message.data}")
    message.ack()
    e.set()


t.start()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}")

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()