import pandas as pd  # For handling CSV

try:
    # 👉 Load the expenses.csv file
    df = pd.read_csv('expenses.csv')
except FileNotFoundError:
    print("❌ No expenses.csv found. Please add expenses using tracker.py first.")
    exit()

# 👉 Show full table
print("\n📄 All Expenses:")
print(df)

# 👉 Show total amount spent
total_spent = df['Amount'].sum()
print(f"\n💰 Total Spent: {total_spent} INR")

# 👉 Show spending by category
print("\n📊 Spending by Category:")
print(df.groupby('Category')['Amount'].sum())

# 👉 (Optional) Show spending by date
print("\n📅 Spending by Date:")
print(df.groupby('Date')['Amount'].sum())

