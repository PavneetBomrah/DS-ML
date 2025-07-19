
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np

df = pd.read_csv("data/StudentsPerformance.csv")

df["Average"] = (df["math score"]+df["reading score"]+df["writing score"])/3
print(df)
df = pd.get_dummies(df,drop_first=True)
print(df)

df['pass/fail'] = df["Average"].apply(lambda x: 1 if x > 50 else 0)
df.drop(["Average"],axis=1)

y = df["pass/fail"]
X = df.drop(["pass/fail"],axis=1)

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print("Model Accuracy :",accuracy_score(y_test,y_pred))
print("Classification Report :\n",classification_report(y_test,y_pred))