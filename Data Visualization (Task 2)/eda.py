import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("churn-bigml-80.csv")

# Histogram
plt.hist(df['Account length'],bins= 15)
plt.title("Distribution Of Account Length")
plt.xlabel('Account length')
plt.ylabel('Frequency')
plt.show()

# Histogram (Point-wise)
# 1. Definition
# A histogram is a graph used to display the distribution of numerical data.
# 2. Purpose
# To understand how the data is distributed.
# To identify the range where most values occur.
# 3. X-Axis
# Represents the numerical values (e.g., Account Length).
# 4. Y-Axis
# Represents the frequency (number of observations).
# 5. Bins
# Data is divided into intervals called bins.
# Each bar represents one range of values.
# 6. Uses
# Understand data distribution.
# Find the most common value range.
# Detect skewness.
# Identify gaps in data.
# Observe the overall pattern of the dataset.
# 7. Example
# plt.hist(df["Account length"], bins=15)
# Column: Account Length
# Bins: 15 intervals
# Output: Shows how many customers fall into each account length range.
# 8. Real-Life Example

# Suppose student marks are:

# 20, 25, 30, 35, 40, 45, 50, 55

# A histogram groups these marks into ranges (e.g., 20–30, 31–40, 41–50) and shows how many students fall into each range.

# 9. Advantages
# Easy to understand.
# Quickly shows data distribution.
# Helps identify patterns and trends.
# Useful for large datasets.


#BOX PLOT
plt.boxplot(df['Account length'])
plt.title("Box Plot of Account Length")
plt.ylabel('Account length')
plt.show()

# Box Plot
# What is a Box Plot?

# A Box Plot is a graph used to summarize the distribution of numerical data.
#  It helps us understand how the data is spread and whether there are any unusual values (outliers).

# Why do we use a Box Plot?
# To detect outliers (unusual values).
# To find the median (middle value).
# To understand the spread of data.
# To compare the distribution of different datasets.
# To check whether the data is skewed or symmetric.

# Main Parts of a Box Plot
# Minimum – Smallest value (excluding outliers).
# Q1 (First Quartile) – 25% of the data lies below this value.
# Median (Q2) – Middle value of the dataset.
# Q3 (Third Quartile) – 75% of the data lies below this value.
# Maximum – Largest value (excluding outliers).
# Outliers – Values that are much higher or lower than the rest of the data.

# Example
# Dataset:
# 10, 12, 13, 15, 16, 18, 20, 22, 80
# Minimum = 10
# Q1 = 13
# Median = 16
# Q3 = 20
# Maximum = 22
# Outlier = 80
# Here, 80 is far away from the other values, so it appears as an outlier.

# Advantages of Box Plot
# Easy to identify outliers.
# Shows the median clearly.
# Summarizes data in one graph.
# Useful for comparing multiple datasets.
# Helps in data cleaning before machine learning.

#SCATTER PLOT
plt.scatter(df['Account length'],df['Total day minutes'])
plt.title("Account Length VS Total Day Minutes")
plt.xlabel("Account Length")
plt.ylabel("Total Day Minutes")
plt.show()

# Scatter Plot
# What is a Scatter Plot?

# A Scatter Plot is a graph used to show the relationship between two numerical variables. Each point on the graph represents one observation (one row of data).

# Why do we use a Scatter Plot?
# To find the relationship between two numerical variables.
# To identify positive correlation.
# To identify negative correlation.
# To detect no correlation.
# To identify outliers.
# To observe patterns and trends in the data.
# What does a Scatter Plot show?
# X-axis → First numerical variable.
# Y-axis → Second numerical variable.
# Each dot → One record (one row) from the dataset.

# Example:

# plt.scatter(df["Account length"], df["Total day minutes"])
# X-axis = Account Length
# Y-axis = Total Day Minutes

# Each dot represents one customer.

# Types of Relationships
# 1. Positive Correlation 📈

# As X increases, Y also increases.

# Example:

# Study Hours ↑ → Marks ↑
# 2. Negative Correlation 📉

# As X increases, Y decreases.

# Example:

# Price ↑ → Demand ↓
# 3. No Correlation

# There is no clear relationship between X and Y.

# The points appear randomly scattered.

# Advantages of Scatter Plot
# Shows the relationship between two variables.
# Easy to identify trends.
# Helps detect outliers.
# Useful before building machine learning models.
# Widely used in Exploratory Data Analysis (EDA).

#CORRELATION MATRIX
print(df.corr(numeric_only=True))


## top 10 states with the highest numbers of customers
# print(df['State'].value_counts().head(10))
#chrun count
print(df["Churn"].value_counts()) #False    2278  True      388
#chrun percentage
print(df["Churn"].value_counts(normalize=True)*100)
#Average Day Minutes
print(df["Total day minutes"].mean())
#Maximum Day Minutes
print(df["Total day minutes"].max())
#Minimum Day Minutes
print(df["Total day minutes"].min())
#Group By
print(df.groupby("Churn")["Total day minutes"].mean())

df.to_csv("cleaned_churn_dataset.csv", index=False)