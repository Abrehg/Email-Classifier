from Final_function import Main_Function
from datetime import datetime
from CreateService import gmailServiceCreate

service = gmailServiceCreate()

def current_time():
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")
   print(current_time)

current_time()
Main_Function()
current_time()