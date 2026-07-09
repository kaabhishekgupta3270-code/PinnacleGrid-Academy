class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_string(self):
        return f"{self.emp_id},{self.name},{self.department},{self.salary}\n"
