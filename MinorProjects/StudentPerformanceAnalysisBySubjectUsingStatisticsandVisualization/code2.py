import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_scores.csv")

def cleanData():
    clean = df.fillna(0)
    subjects = ["Maths","Science","English","SST"]
    for index,row in clean.iterrows():
        
cleanData()