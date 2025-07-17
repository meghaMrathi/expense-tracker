import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create DB & table once
def create_table():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense():
    # INSERT new row to DB
    ...

def show_summary():
    # SELECT rows, show with pandas
    ...

def show_chart():
    # SELECT rows, plot with matplotlib
    ...

def predict_spending():
    # SELECT rows, group with pandas, use ML
    ...

# Main menu
create_table()  # runs once
while True:
    print("1) Add Expense")
    print("2) Show Summary")
    print("3) Show Chart")
    print("4) Predict")
    print("5) Exit")
    choice = input("Choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_summary()
    elif choice == '3':
        show_chart()
    elif choice == '4':
        predict_spending()
    elif choice == '5':
        break
    else:
        print("Invalid")
