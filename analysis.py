# 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
import pandas as pd
import numpy as np

df = pd.read_csv("/home/niteshpant/Desktop/glassdoorAnalysis/Uncleaned_DS_jobs.csv")

#print(df.head(10))
#print(df.columns)
#print(df.shape)
#print(df.info())
#print(df.isnull().sum())

'''
    Make the salary column into integers
'''
def convertSalary(salary, df):
    Min_Salary = []
    Max_Salary = []

    for sal in range(len(salary)):
        min = salary[sal][0]
        min = str(min).replace('K', '')
        Min_Salary.append(int(min) * 1000)
        max = salary[sal][1]
        max = str(max).replace('K', '') 
        Max_Salary.append(int(max) * 1000)

    df['Min Salary'] = Min_Salary
    df['Max Salary'] = Max_Salary

    return df[['Min Salary', 'Max Salary']]

#print(df['Salary Estimate'].head(20))
#print(df['Salary Estimate'].unique())
df['Salary Estimate2'] = df['Salary Estimate'].str.rstrip(' (Glassdoor est.)').str.replace('$', '').str.strip('(Employ').str.split('-')
df[['Min Salary', 'Max Salary']] = convertSalary(df['Salary Estimate2'], df)
#print(df[['Min Salary', 'Max Salary', 'Salary Estimate', 'Salary Estimate2']].head())

'''
    What information can you extract out of job descriptions?
    Remove the numbers from the company name?
    Create some new features? (e.g. state column from the location column)
'''
