import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("country_wise_latest.csv")

print(df.head())
print("Shape:", df.shape)
print("\nColumns:", df.columns)

print(df.describe())
print(df.info())
top10_confirmed = df.sort_values(by='Confirmed', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top10_confirmed, x='Confirmed', y='Country/Region', palette='Reds_r')
plt.title('Top 10 Countries by Confirmed Cases')
plt.xlabel('Confirmed Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.show()
df['Death Rate (%)'] = (df['Deaths'] / df['Confirmed']) * 100
df['Recovery Rate (%)'] = (df['Recovered'] / df['Confirmed']) * 100

top_death_rate = df.sort_values(by='Death Rate (%)', ascending=False).head(10)
print(top_death_rate[['Country/Region', 'Death Rate (%)', 'Confirmed']])
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Confirmed', 'Deaths', 'Recovered', 'Active']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
