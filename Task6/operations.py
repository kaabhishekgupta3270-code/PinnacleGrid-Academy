from employee import Employee

FILE_NAME = "employees.txt"


def add_employee():
    try:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(emp_id, name, department, salary)

        with open(FILE_NAME, "a") as file:
            file.write(employee.to_string())

        print("\nEmployee Added Successfully.")

    except ValueError:
        print("Invalid Salary.")


def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("\nNo Employees Found.")
                return

            print("\n------ Employee Records ------")
            for emp in data:
                emp = emp.strip().split(",")

                print(f"ID         : {emp[0]}")
                print(f"Name       : {emp[1]}")
                print(f"Department : {emp[2]}")
                print(f"Salary     : {emp[3]}")
                print("-" * 30)

    except FileNotFoundError:
        print("Employee file not found.")


def search_employee():
    emp_id = input("Enter Employee ID: ")

    try:
        with open(FILE_NAME, "r") as file:
            for emp in file:
                data = emp.strip().split(",")

                if data[0] == emp_id:
                    print("\nEmployee Found")
                    print(f"ID         : {data[0]}")
                    print(f"Name       : {data[1]}")
                    print(f"Department : {data[2]}")
                    print(f"Salary     : {data[3]}")
                    return

        print("Employee Not Found.")

    except FileNotFoundError:
        print("Employee file not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            employees = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for emp in employees:
                data = emp.strip().split(",")

                if data[0] != emp_id:
                    file.write(emp)
                else:
                    found = True

        if found:
            print("Employee Deleted Successfully.")
        else:
            print("Employee Not Found.")

    except FileNotFoundError:
        print("Employee file not found.")


def update_employee():
    emp_id = input("Enter Employee ID to Update: ")

    try:
        with open(FILE_NAME, "r") as file:
            employees = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:

            for emp in employees:

                data = emp.strip().split(",")

                if data[0] == emp_id:

                    name = input("Enter New Name: ")
                    department = input("Enter New Department: ")
                    salary = input("Enter New Salary: ")

                    file.write(f"{emp_id},{name},{department},{salary}\n")

                    found = True

                else:
                    file.write(emp)

        if found:
            print("Employee Updated Successfully.")
        else:
            print("Employee Not Found.")

    except FileNotFoundError:
        print("Employee file not found.")
