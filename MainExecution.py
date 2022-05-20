print("Email Sorting using the Decision Trees Model")
print("A project by Adityaa Suratkal")
print("Started on 1/1/22")
print("Finished on 4/15/22")
import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
from Final_function import Main_Function
from CreateService import gmailServiceCreate
from datetime import datetime
import threading

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

def wait_for_event(e):
    while True:
        print("Starting the main function")
        event_is_set = e.wait()
        Main_Function()
        e.clear()

current_time()

credentials_path = """Enter service key here"""
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
    now = datetime.now()
    time_now = now.strftime("%H")
    if time_now == "09":
        search_new_message()
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