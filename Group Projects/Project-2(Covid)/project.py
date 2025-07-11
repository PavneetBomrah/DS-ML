import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def pieAllDRARatio():
    df = pd.read_csv('country_wise_latest.csv')
    df = df[['Country/Region','Deaths','Recovered','Active']]
    label=['Deaths','Recovered','Active']
    plt.pie([df['Deaths'].sum(),df['Recovered'].sum(),df['Active'].sum()], labels=label, colors=['#ff0000','#00ff00','#0000ff'])
    plt.title('Death, Recovered and Active Cases Ratio')
    plt.show()
    print(df['Deaths'].sum(),df['Recovered'].sum(),df['Active'].sum())

def pieDRARatio(country):
    df = pd.read_csv('country_wise_latest.csv')
    dfc = df[df['Country/Region'] == country]
    label=['Deaths','Recovered','Active']
    plt.pie([df['Deaths'].sum(),df['Recovered'].sum(),df['Active'].sum()], labels=label, colors=['#ff0000','#00ff00','#0000ff'])
    plt.title(f'Death, Recovered and Active Cases Ratio of {country.upper()}')
    plt.show()
    print(dfc)

def barAllDROH():
    df = pd.read_csv('country_wise_latest.csv')
    df = df[['Country/Region', 'Deaths / 100 Cases', 'Recovered / 100 Cases']]
    death_ratio = df['Deaths / 100 Cases'].mean()
    recovered_ratio = df['Recovered / 100 Cases'].mean()
    labels = ['Deaths / 100 Cases', 'Recovered / 100 Cases']
    values = [death_ratio, recovered_ratio]
    plt.bar(labels, values, color=['red', 'green'])
    plt.title('Death and Recovered per 100 Cases (Average Across Countries)')
    plt.ylabel('Avg per 100 Cases')
    plt.show()

def barDROH(country):
    df = pd.read_csv('country_wise_latest.csv')
    dfc = df[df['Country/Region'] == country]
    dfc = dfc[['Country/Region', 'Deaths / 100 Cases', 'Recovered / 100 Cases']]
    death_ratio = dfc['Deaths / 100 Cases'].sum()
    recovered_ratio = dfc['Recovered / 100 Cases'].sum()
    labels = [f'Deaths / 100 Cases ({death_ratio})', f'Recovered / 100 Cases ({recovered_ratio})']
    values = [death_ratio, recovered_ratio]
    plt.bar(labels, values, color=['red', 'green'])
    plt.title(f'Death and Recovered per 100 Cases in {country}')
    plt.ylabel('Avg per 100 Cases')
    plt.show()

def plotRegionDeath():
    df = pd.read_csv('country_wise_latest.csv')
    region_deaths = df.groupby('WHO Region')['Deaths'].sum()
    plt.figure(figsize=(10,6))
    plt.bar(region_deaths.index, region_deaths.values, color='skyblue')
    plt.xticks(rotation=45)
    plt.title('Total Deaths by WHO Region')
    plt.xlabel('WHO Region')
    plt.ylabel('Number of Deaths')
    plt.tight_layout()
    plt.show()

def plotRegionRecovered():
    df = pd.read_csv('country_wise_latest.csv')
    region_recovers = df.groupby('WHO Region')['Recovered'].sum()
    plt.figure(figsize=(10,6))
    plt.bar(region_recovers.index, region_recovers.values, color='skyblue')
    plt.xticks(rotation=45)
    plt.title('Total Recovered by WHO Region')
    plt.xlabel('WHO Region')
    plt.ylabel('Number of Recovered')
    plt.tight_layout()
    plt.show()

def plotRegionActive():
    df = pd.read_csv('country_wise_latest.csv')
    region_active = df.groupby('WHO Region')['Active'].sum()
    plt.figure(figsize=(10,6))
    plt.bar(region_active.index, region_active.values, color='skyblue')
    plt.xticks(rotation=45)
    plt.title('Total Active by WHO Region')
    plt.xlabel('WHO Region')
    plt.ylabel('Number of Active')
    plt.tight_layout()
    plt.show()

while True:    
    print('\n\n','*'*30)
    choice = input('''
        Welcome to Covid Reporter

    1. Pie Chart of Death Recovere and Active Ratio
    2. Pie Chart of Death Recovere and Active Ratio (Country)
    3. Bar Grapg of Death and Recovery out of 100s
    4. Bar Grapg of Death and Recovery out of 100s (Country)
    5. Death by WHO Regions
    6. Recovered by WHO Regions
    7. Active by WHO Regions
    0. Exit

    Enter your Input: 
    ''')

    match choice:
        case '1':
            print("Showing Pie Chart of Death Recovere and Active Ratio")
            pieAllDRARatio()
        case '2':
            country = input("Enter Country Name")
            print("Showing Pie Chart of Death Recovere and Active Ratio (Country)")
            pieDRARatio(country)
        case '3':
            print("Showing Bar Grapg of Death and Recovery out of 100s")
            barAllDROH()
        case '4':
            country = input("Enter Country Name")
            print("Showing Bar Grapg of Death and Recovery out of 100s (Country)")
            barDROH(country)
        case '5':
            print("Showing Death by WHO Regions")
            plotRegionDeath()
        case '6':
            print("Showing Recovered by WHO Regions")
            plotRegionRecovered()
        case '7':
            print("Showing Active by WHO Regions")
            plotRegionActive()
        case _:
            break
    print('\n\n','*'*30)
