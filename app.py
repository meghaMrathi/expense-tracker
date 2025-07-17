import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount spent: "))

    new_expense = {'Date': date, 'Category': category, 'Amount': amount}

    try:
        df = pd.read_csv('expenses.csv')
        new_row = pd.DataFrame([new_expense])
        df = pd.concat([df, new_row], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([new_expense])

    df.to_csv('expenses.csv', index=False)
    print("Expense saved.\n")

def show_summary():
    try:
        df = pd.read_csv('expenses.csv')
    except FileNotFoundError:
        print("No expenses.csv found. Please add expenses first.\n")
        return

    print("\nAll Expenses:")
    print(df)

    total_spent = df['Amount'].sum()
    print(f"\nTotal Spent: {total_spent} INR")

    print("\nSpending by Category:")
    print(df.groupby('Category')['Amount'].sum())

    print("\nSpending by Date:")
    print(df.groupby('Date')['Amount'].sum())
    print()

def show_chart():
    try:
        df = pd.read_csv('expenses.csv')
    except FileNotFoundError:
        print("No expenses.csv found. Please add expenses first.\n")
        return

    category_summary = df.groupby('Category')['Amount'].sum()
    category_summary.plot(kind='bar')

    plt.title('Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Spent (INR)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def predict_spending():
    try:
        df = pd.read_csv('expenses.csv')
    except FileNotFoundError:
        print("No expenses.csv found. Please add expenses first.\n")
        return

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_spending = df.groupby('Month')['Amount'].sum().reset_index()
    monthly_spending['Month_Num'] = range(1, len(monthly_spending) + 1)

    X = monthly_spending['Month_Num'].values.reshape(-1, 1)
    y = monthly_spending['Amount'].values

    model = LinearRegression()
    model.fit(X, y)

    next_month = [[len(monthly_spending) + 1]]
    predicted_spending = model.predict(next_month)

    print(f"\nPredicted spend for next month: {predicted_spending[0]:.2f} INR\n")

while True:
    print("========== Expense Tracker ==========")
    print("1) Add Expense")
    print("2) Show Summary")
    print("3) Show Chart")
    print("4) Predict Next Month Spend")
    print("5) Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_summary()
    elif choice == '3':
        show_chart()
    elif choice == '4':
        predict_spending()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")
