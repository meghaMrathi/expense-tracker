import pandas as pd
import matplotlib.pyplot as plt

# Load the expenses data
df = pd.read_csv('expenses.csv')

# Group by category and sum amounts
category_summary = df.groupby('Category')['Amount'].sum()

# Make a bar chart
category_summary.plot(kind='bar')

plt.title('Spending by Category')
plt.xlabel('Category')
plt.ylabel('Total Spent (INR)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Spending over time
date_summary = df.groupby('Date')['Amount'].sum()

date_summary.plot(kind='line', marker='o')

plt.title('Spending Over Time')
plt.xlabel('Date')
plt.ylabel('Total Spent (INR)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
