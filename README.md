***How it works***

Using the Gmail API and Pub Sub API by Google, the model listens for activity in the inbox using the Pub Sub API. 

Once activity is detected, a separate thread with the Gmail API and the main model captures the data in the new email and uses it for classification

After the data is captured by the program, the data is cleaned using the text normalization function in the file titled “text_parsing” and the LDA model

Input data is then used by the Decision Trees model to find a classification for the email

The output of the Decision Trees model is then taken by the Google API and does whatever you have assigned it to do to that classification (send it to trash, add a label, remove a label, etc.)

Then, the thread stops, and the Pub-Sub API will continue to listen for new activity

Once the model is running properly, inbox can be cleared of labeled emails by running the “cleanSlate” file. Emails to be removed must be labeled in order for the file to work properly.

***Environment setup***

**Must use:**

Python 3.7 and up (I used python 3.9.6)

**Download the following packages (if not already downloaded):**

Collections

Concurrent

Contractions (only download version 0.0.18)

Datetime

Emoji

Gensim

Google

Httplib2

MatPlotLib

Nltk

Numpy

OS

Pandas

Pickle

Regular expressions (re)

Seaborne

SkLearn

Threading

Uritemplate

Note: For the nltk package, run the file “installnltk” in the preferred environment. A menu should come up prompting you what data to download. Download all the data available

If you don’t have the pubsub_v1 package when you download the google package, run pip install --upgrade google-cloud-pubsub inside terminal or command line based on OS.

***Customization***

Before doing any other customization, you need to create an account in the Google API website (https://console.cloud.google.com) and create a client ID. Once you have created the client ID, you must download it and add it to the project folder. Then, in the file named “CreateService”, you will need to type in the name of the file (along with .json) in the “CLIENT FILE” variable as a string.

Then, you need to create a service account for the Pub-Sub API and add its corresponding json file to the project folder. The json file can be downloaded directly from the Google APIs website. To make the Pub-Sub API work, you must type in the name of the file under the variable “credentials_path” as a string, while also including the .json file format. 

Once you have the required credential files, you must determine the different labels that you will sort your email into. You must also decide what numerical labels you will use in the program. The labels that I started with were Normal, Interpersonal, Promotional, and College, and their corresponding numerical labels were 0, 1, 2, and 3. All of these labels and numerical labels must be held constant throughout the program.

Create these labels in Gmail and label all of the emails you can with your desired labels (one per email and no label for normal mails). Also find the name of the label that google recognizes (you can find this using the “labels.list” documentation on the Gmail API website and use the trial option to see what all of the labels are named (Inbox is always “INBOX”). Once you do that, paste the names in new variables as strings in the file "CreateService". Then you can import these variables to all of the files that need the labels (cleanSlate, trainingDataCreation, LDAtrainingDataCreation, final_function) (delete mine from the import statements section)

For ease of use, assign these names to variables that correspond to the intended labels in the “LDAtrainingDataCreation” file, the “Final_function” file (close to the end of the file), the “cleanSlate” file, and the “trainingDataCreation” file.

In the “LDAtrainingDataCreation” file, you must change lines 71 - 96 to generate a list of Ids in each label by using the same format as the one used for sent ids. The names of the different variables can be changed as per preference, but one loop is needed for each label. To change the label that the loop focuses on, you must switch out one value in the function “search_messages” from “SENT” to the corresponding variable for the label (“must be a string”)

After you modify lines 71 - 96, you need to modify lines 190 - 211 of the original “LDAtrainingDataCreation” file. You need to modify the nested loops by adding a nested while loop for each label. Each loop uses the label name variable, the variable for the list created earlier, and the corresponding numeric label for each respective email will be set equal to the respective row in column 5 (list format), then the corresponding row in the list created earlier will be popped. 

In the “trainingDataCreation” file, the changes from “LDAtrainingDataCreation” can be copied and pasted onto the “trainingDataCreation” file. The location of these changes are also similar in both files.

In the “Final_function” file, lines 200 - 215 need to be modified to fit your desired action. The classification variable contains the output of the main machine learning model and will contain one of your numeric labels. You must create an if statement and elif statement where if the classification variable contains a numeric label, the program will do something. Functions have already been added to the file which do certain things. “add_label” adds a certain label to the provided email given the service, desired label to be added, and id variables. “trash_message” sends an email into the gmail trash can given the service and id variables. “remove_label” removes a certain label from an email given the service, label, and id variables. id variable has already been declared in program, only the word “id” needs to be typed into the function. 

In the “cleanSlate” file, lines 30 - 63 need to be modified in order to fit your desired labels. The file already contains the functions “trash_message” and “remove_label” and takes in the same variables as the one in the “Final_function” file. For each label, you first use the “search_messages” function to find all of the emails and store it in a variable. Then, in a while loop, you append variable["messages"][ctr]["id"] to the end of a separate list (ctr is a variable that is less than the length of the result from “search_messages”). Once that is done, you use a separate for loop to use a function on every id in the list.

In the “LDATrain” file, comment out lines 52-67 and then remove the triple quotes around lines 68 and 152. Once finished, you can run the file in order to find the optimal number of topics that should be used by the model using the graph that is generated once the file is run. The optimal topic should maximize coherence and minimize the topic overlap, both of which will be shown by the graph generated by the program once run. Once you find the optimal number of topics to use, you can create a multiline comment around lines 69-151 and remove the triple quotes around lines 52-67. Then, you can update the number stored in the variable “num_topics” to be the one found by using the graph. If any of the rows in the training data don’t work, add the row index to the lists on lines 13 and 15 (list in line 13 is a part of the drop function) 

Once you finish these modifications to the original program, the entire program is ready to run.

***Execution***

Once completely customized, run the files in the following order and restart if any errors come up:

1. Installnltk (install all data available)
2. LDAtrainingDataCreation
3. LDATrain
4. trainingDataCreation
5. Tree_train
6. TestExecution (can be skipped if you don’t want to test the model)
7. MainExecution (runs indefinitely)
8. cleanSlate (to clear out your inbox)
