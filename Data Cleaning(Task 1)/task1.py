import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("churn-bigml-80.csv")
print(df.head()) 
print(df.shape) 
print(df.columns) 
print(df.info()) 
print(df.isnull().sum()) 
print(df.isnull().sum().sum()) 
print(df.duplicated())
print(df.duplicated().sum()) 
print(df.describe()) 
print(df['Account length'].median()) 
print(df.columns.tolist())
print(df['Account length'].mean())
print(df['State'].mode()) 
print(df['State'].unique()) 
print(df['State'].nunique())  
print(df['State'].value_counts()) 
print(df['State'].describe()) 








