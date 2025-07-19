import os
import pandas as pd
import zipfile
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Setup Kaggle API (Fill your credentials)
os.environ['KAGGLE_USERNAME'] = "pavneetbomrah"
os.environ['KAGGLE_KEY'] = "1eeb684317cd5c6b03f235b4bff27dbf"

# Step 2: Download Dataset
# ~kaggle datasets download -d spscientist/students-performance-in-exams

# Step 3: Unzip
with zipfile.ZipFile("students-performance-in-exams.zip", 'r') as zip_ref:
    zip_ref.extractall("data")

# Step 4: Load Dataset
df = pd.read_csv("data/StudentsPerformance.csv")
print("Data Loaded Successfully!\n", df.head())

# Step 5: Feature Engineering
df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3
df['pass/fail'] = df['average_score'].apply(lambda x: 1 if x >= 50 else 0)
df = df.drop(['average_score'], axis=1)

# Encode categorical variables
print(df.head())
df = pd.get_dummies(df, drop_first=True)
print(df.head())

# Step 6: Prepare features and target
X = df.drop('pass/fail', axis=1)
y = df['pass/fail']

# Step 7: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 8: Train Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 9: Predict and Evaluate
y_pred = model.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 10: Optional Visualization
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()
