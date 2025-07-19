
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

df = pd.read_csv("data/StudentsPerformance.csv")

print(df.head())