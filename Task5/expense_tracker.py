FILE_NAME = "expenses.txt"


# Add Expense
def add_expense():
    try:
        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: ₹"))

        with open(FILE_NAME, "a") as file:
            file.write(f"{date},{category},{amount}\n")

        print("\nExpense added successfully!")

    except ValueError:
        print("\nInvalid amount! Please enter numbers only.")


# View Expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if len(expenses) == 0:
            print("\nNo expenses found.")
            return

        print("\n========== Expense List ==========")

        for i, expense in enumerate(expenses, start=1):
            date, category, amount = expense.strip().split(",")

            print(f"\nExpense No : {i}")
            print(f"Date        : {date}")
            print(f"Category    : {category}")
            print(f"Amount      : ₹{amount}")
            print("-" * 30)

    except FileNotFoundError:
        print("\nNo expense file found.")


# Delete Expense
def delete_expense():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if len(expenses) == 0:
            print("\nNo expenses available.")
            return

        view_expenses()

        number = int(input("\nEnter Expense Number to Delete: "))

        if 1 <= number <= len(expenses):

            expenses.pop(number - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(expenses)

            print("\nExpense deleted successfully!")

        else:
            print("\nInvalid expense number.")

    except FileNotFoundError:
        print("\nNo expense file found.")

    except ValueError:
        print("\nPlease enter a valid number.")


# Total Spending
def total_spending():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:

            for expense in file:
                date, category, amount = expense.strip().split(",")
                total += float(amount)

        print(f"\nTotal Spending = ₹{total}")

    except FileNotFoundError:
        print("\nNo expense file found.")


# Main Menu
while True:

    print("\n===============================")
    print("      Expense Tracker")
    print("===============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        total_spending()

    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Please try again.")
