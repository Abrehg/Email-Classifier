import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
import pickle

X = []
y = []
data = pd.read_csv("Model_Data.csv")
data = data.drop(columns=['Id', 'Subject', 'Body', 'Unnamed: 0'], axis=1)
i = 0
instance = []
while i < len(data):
    y.append(data.iat[i,4])
    instance = []
    j = 0
    while j < 4:
        instance.append(data.iat[i,j])
        j = j + 1
    X.append(instance)
    i = i + 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
DT = tree.DecisionTreeClassifier()
DT.fit(X_train, y_train)
result = DT.score(X_test, y_test)
print(result)

filename = 'finalized_model.sav'
pickle.dump(DT, open(filename, 'wb'))