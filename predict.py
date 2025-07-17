import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# 👉 Load your data
df = pd.read_csv('expenses.csv')

# ✅ For a simple example — let’s pretend each date is a separate month
# Make sure dates are sorted
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Group by month
df['Month'] = df['Date'].dt.to_period('M')
monthly_spending = df.groupby('Month')['Amount'].sum().reset_index()

print("\n📅 Monthly Spending:")
print(monthly_spending)

# 👉 For ML: we need X and y
# X = month number [1, 2, 3...]
# y = total spending for that month
monthly_spending['Month_Num'] = range(1, len(monthly_spending) + 1)

X = monthly_spending['Month_Num'].values.reshape(-1, 1)
y = monthly_spending['Amount'].values

# ✅ Train Linear Regression
model = LinearRegression()
model.fit(X, y)

# ✅ Predict next month
next_month = [[len(monthly_spending) + 1]]
predicted_spending = model.predict(next_month)

print(f"\n💡 Predicted spend for next month: {predicted_spending[0]:.2f} INR")
