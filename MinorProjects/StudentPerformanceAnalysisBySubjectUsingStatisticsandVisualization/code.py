import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

df = pd.read_csv("student_scores.csv")

def dataClean():
    df_clean = df.fillna(0).copy()
    subjects = ["Maths", "Science", "English", "SST"]

    print("Name\tMaths\tScience\tEnglish\tSST")
    for index, row in df_clean.iterrows():
        print(f"{row['Student']}", end="\t")
        for subject in subjects:
            score = row[subject]
            if 0 <= score <= 100:
                print(int(score), end="\t")
            else:
                print("err", end="\t")
                df_clean.at[index, subject] = 0 
        print()
    
    return df_clean

def descriptiveStats(df):
    subjects = ["Maths", "Science", "English", "SST"]
    print("\nDescriptive Statistics:")
    for subject in subjects:
        print(f"\n{subject}:")
        print(f"  Mean    : {df[subject].mean():.2f}")
        print(f"  Median  : {df[subject].median():.2f}")
        try:
            print(f"  Mode    : {mode(df[subject])}")
        except:
            print("  Mode    : No unique mode")
        print(f"  Standard Deviation : {df[subject].std():.2f}")
        print(f"  Variance: {df[subject].var():.2f}")
    
    avg_scores = {subject: df[subject].mean() for subject in subjects}
    most = max(avg_scores, key=avg_scores.get)
    least = min(avg_scores, key=avg_scores.get)
    print(f"\nMost Scoring Subject   : {most}")
    print(f"Least Scoring Subject  : {least}")

def studentWiseAnalysis(df):
    print("\nStudent-wise Analysis:")
    for index, row in df.iterrows():
        total = row[["Maths", "Science", "English", "SST"]].sum()
        avg = total / 4
        print(f"{row['Student']:<10} Total: {int(total):<3} Avg: {avg:.2f}")

def subjectWiseTopper(df):
    print("\nSubject-wise Toppers:")
    subjects = ["Maths", "Science", "English", "SST"]
    for subject in subjects:
        max_score = df[subject].max()
        toppers = df[df[subject] == max_score]["Student"].tolist()
        print(f"{subject}: {', '.join(toppers)} ({max_score})")

def visualize(df):
    subjects = ["Maths", "Science", "English", "SST"]

    df["Total"] = df[subjects].sum(axis=1)
    plt.figure(figsize=(10, 5))
    plt.bar(df["Student"], df["Total"], color="skyblue")
    plt.title("Total Marks per Student")
    plt.xlabel("Student")
    plt.ylabel("Total Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    subject_averages = [df[subject].mean() for subject in subjects]
    plt.figure()
    plt.plot(subjects, subject_averages, marker='o', linestyle='-', color='green')
    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.grid(True)
    plt.show()

    plt.figure()
    df[subjects].plot(kind='box')
    plt.title("Spread of Marks per Subject")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

    for subject in subjects:
        plt.figure()
        plt.hist(df[subject], bins=10, color='orange', edgecolor='black')
        plt.title(f"Histogram - {subject}")
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()


df_cleaned = None

while True:
    print("*" * 40)
    print("\t\tMenu\n")
    print("""
        1. Data Cleaning
        2. Descriptive Statistics
        3. Student-Wise Analysis
        4. Subject-Wise Topper
        5. Visualization
        0. Exit
    """)
    print("*" * 40)


    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("\nCleaning Data...\n")
        df_cleaned = dataClean()

    elif choice == "2":
        if df_cleaned is not None:
            descriptiveStats(df_cleaned)

        else:
            print("Please clean data first (Option 1)")

    elif choice == "3":
        if df_cleaned is not None:
            studentWiseAnalysis(df_cleaned)
        else:
            print("Please clean data first (Option 1)")

    elif choice == "4":
        if df_cleaned is not None:
            subjectWiseTopper(df_cleaned)
        else:
            print("Please clean data first (Option 1)")

    elif choice == "5":
        if df_cleaned is not None:
            visualize(df_cleaned)
        else:
            print("Please clean data first (Option 1)")

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid option. Try again.")
