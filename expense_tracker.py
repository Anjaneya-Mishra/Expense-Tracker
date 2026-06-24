import pandas as pd
import os

file_name = "expense_2.csv"

def add_expense():
    Date = int(input("Enter the Date: "))
    Month = input("Enter the Month: ")
    Category = input("Enter the Category (Food/Shopping/Travel/Others): ")
    Amount = float(input("Enter the Amount: "))

#data directly entered into the Dataframe 

    new_expense = pd.DataFrame({
        "Date": [Date],
        "Month": [Month],
        "Category": [Category],
        "Amount": [Amount]
    })

    if os.path.exists(file_name):
        old_data = pd.read_csv(file_name)
        updated_data = pd.concat([old_data, new_expense], ignore_index=True)
    else:
        updated_data = new_expense # the data we just put in will be entered in the file 

    updated_data.to_csv(file_name, index=False)

    print("Expense added successfully!")


def view_expenses():
#This part is because what if the user enters choice 2 first to view expense, then what if the file doesn't exist. Therefore for that we return No expense found 
    if not os.path.exists(file_name):
        print("No expenses found.")
        return
#reads all the expenses ( We are reading this because we want to print )
    df = pd.read_csv(file_name) # reading file as df
#showing all the expenses in the file 
    print("\nAll Expenses")
    print(df)

def show_summary():
#This part is because what if the user enters choice 3 first to show summary, then what if the file doesn't exist. Therefore for that we return No expense found 
    if not os.path.exists(file_name):
        print("No expenses found.")
        return
        
    df = pd.read_csv(file_name) #reading as df for this function 

    #for total amount 
    total_amount = df["Amount"].sum()
    print("\nTotal Amount Spent:-",total_amount)
    #for Amount spent per category 
    print("\nAmount Spent Category-wise")
    category_total = df.groupby("Category")["Amount"].sum()
    print(category_total)


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary")
    print("4. Exit")
    choice = input("Choose option: ")
    
    if choice == "1":
        # call which function?
        add_expense()
    elif choice == "2":
        # call which function?
        view_expenses()
    elif choice == "3":
        # call which function?
        show_summary()
    elif choice == "4":
        print("Exiting.....")
        break 
    else:
        print("Invalid Choice. Try again!")
        