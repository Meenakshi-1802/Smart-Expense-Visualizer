import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

# Connect to MySQL
try:
    connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2018",
    database="ExpenseDB",
    connection_timeout=10
)
    cursor = connect.cursor()
    print("Connected to MySQL successfully!")
except mysql.connector.Error as err:
    print(f"Error:{err}")
    exit()

# Function to add expenses
def add_expense(Category, Amount, Date):
    query = "INSERT INTO Expenses(Category, amount, date) VALUES (%s, %s, %s)"
    values = (Category, Amount, Date)
    cursor.execute(query, values)
    connect.commit()
    print(f"Added Expense: {Category} - ₹{Amount} on {Date}")

# Add sample expenses
add_expense("Food", 500, "2025-03-30")
add_expense("Transport", 200, "2025-03-29")
add_expense("Shopping", 2000, "2025-03-05")
add_expense("Rent", 5000, "2025-03-01")
add_expense("Entertainment", 800, "2025-03-25")
add_expense("Bill", 2000, "2025-03-24")
add_expense("Medicine", 300, "2025-03-20")
add_expense("Grocery", 1000, "2025-03-06")

# Function to get expenses from database
def get_expenses():
    cursor.execute("SELECT Category, Amount FROM Expenses")
    data = cursor.fetchall()
    if not data:
        print("No expenses found!")
        return [], []
    Categories, Amounts = zip(*data)
    return Categories, np.array(Amounts)

# Function to visualize expenses
def visualize_expenses():
    Categories, Amounts = get_expenses()
    if len(Categories) == 0:
        print("No expenses to visualize!")
        return
    plt.figure(figsize=(8, 5))
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'cyan', 'pink', 'yellow']
    plt.bar(Categories, Amounts, color=colors[:len(Categories)])
    plt.xlabel("Categories")
    plt.ylabel("Amount (₹)")
    plt.title("Expense Visualization")
    plt.xticks(rotation=35)
    plt.show(block=True)



#Main Menu(User Interaction)
while True:
    print("Smart Expense Visualizer\n")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Visualize Expenses")
    print("4.Exit")

    choice = input("Please Enter your choice:")

    if choice == "1":
        Category = input("Enter Categories:")
        Amount = int(input("Enter Amount (₹):"))
        Date = input("Enter date(YYYY-MM-DD):")
        add_expense(Category,Amount,Date)

    elif choice == "2":
        Categories,Amounts = get_expenses()
        if len(Categories) > 0:
            print("Expense Records:\n")
            for Cat,Amt in zip(Categories,Amounts):
                print(f"-{Cat} : {Amt}")

    elif choice == "3":
        visualize_expenses()

    elif choice == "4":
        print("Exiting....GoodBye!")
        connect.close()
        break

    else: 
        print("Invalid Choice! Please Enter a valid option.")