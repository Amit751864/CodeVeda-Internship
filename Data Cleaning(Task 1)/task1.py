import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("churn-bigml-80.csv")
print(df.head()) # iska kaam ha ki  first 5 row print
print(df.shape) # ya (row ,column )
print(df.columns) # ya tumko columns ka naam print karega 
print(df.info()) # ya tumko tumhare data ka summary provide karega
print(df.isnull().sum()) # isme apko batya ga ki kitna null value haa 0
print(df.isnull().sum().sum()) # isme pura calculate kar ke bata thaaa haa
print(df.duplicated())# iska matlab ha ki false  = no duplicate rows, but true give dupliccate row in your data
print(df.duplicated().sum()) # ya pura count kar ke bata haa
print(df.describe()) #isme stastic bata ha mean = count, mean, std, min . 25%,50%,75%,max
print(df['Account length'].median()) # ya function are provide  are mid value  in column are account length
print(df.columns.tolist())
print(df['Account length'].mean())
print(df['State'].mode()) # ya bta ha ki kitne kio column me reapat hua haa
print(df['State'].unique()) # ya function are provide kitne unique value haa
print(df['State'].nunique())  # ya function are provide are total unique value
print(df['State'].value_counts()) # ya kitne bar repeat huaaa ya batya gaa
print(df['State'].describe()) # count     2666
# unique      51
# top         WV
# freq        88
#day 5 data vizualistion aaj hum matplotlib use karge






