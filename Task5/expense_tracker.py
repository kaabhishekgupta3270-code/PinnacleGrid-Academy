FILE_NAME = "expenses.txt"


def add_expense():
    try:
        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        with open(FILE_NAME, "a") as file:
            file.write(f"{date},{category},{amount}\n")

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount. Please enter a number.")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No expenses found.")
                return

            print("\n------ Expenses ------")
            for expense in data:
                date, category, amount = expense.strip().split(",")
                print(f"Date: {date}")
                print(f"Category: {category}")
                print(f"Amount: ₹{amount}")
                print("-" * 25)

    except FileNotFoundError:
        print("No expense file found.")


def delete_expense():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses available.")
            return

        view_expenses()

        index = int(input("Enter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            expenses.pop(index)

            with open(FILE_NAME, "w") as file:
                file.writelines(expenses)

            print("Expense deleted successfully!")

        else:
            print("Invalid expense number.")

    except FileNotFoundError:
        print("No expense file found.")

    except ValueError:
        print("Please enter a valid number.")


def total_spending():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            for expense in file:
                _, _, amount = expense.strip().split(",")
                total += float(amount)

        print(f"\nTotal Spending: ₹{total}")

    except FileNotFoundError:
        print("No expense file found.")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        total_spending()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
