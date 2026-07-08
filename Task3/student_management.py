students = []


def add_student():
    student = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Student Name: "),
        "course": input("Enter Course: "),
        "marks": input("Enter Marks: ")
    }
    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\n----- Student Records -----")
    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Course : {student['course']}")
        print(f"Marks  : {student['marks']}")
        print("-" * 25)


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["course"] = input("Enter New Course: ")
            student["marks"] = input("Enter New Marks: ")
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
