# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
file_path =  'C:/Users/Win 10/Downloads/Day_10_banking_data.csv'  # Replace with the actual path
banking_data = pd.read_csv(file_path)

# 1. Bar Plot: Total sum of Transaction_Amount per Account_Type
transaction_sum_by_account_type = banking_data.groupby('Account_Type')['Transaction_Amount'].sum()

# Plotting the bar plot
plt.figure(figsize=(8, 6))
transaction_sum_by_account_type.plot(kind='bar', color='skyblue')
plt.title('Total Transaction Amount by Account Type')
plt.xlabel('Account Type')
plt.ylabel('Total Transaction Amount')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Pie Chart: Percentage of transactions per Branch
transaction_count_by_branch = banking_data['Branch'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
transaction_count_by_branch.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Percentage of Transactions per Branch')
plt.ylabel('')  # Remove y-axis label for better aesthetics
plt.show()