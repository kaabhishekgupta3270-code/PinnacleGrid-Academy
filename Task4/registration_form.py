import tkinter as tk
from tkinter import ttk, messagebox

def submit():
    name = name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    course = course_var.get()

    skills = []

    if python_var.get():
        skills.append("Python")
    if sql_var.get():
        skills.append("SQL")
    if excel_var.get():
        skills.append("Excel")

  
    if name == "" or email == "" or gender == "" or course == "Select Course":
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    result = f"""
Registration Successful!

Name : {name}
Email : {email}
Gender : {gender}
Course : {course}
Skills : {', '.join(skills)}
"""

    messagebox.showinfo("Student Information", result)


root = tk.Tk()
root.title("Student Registration Form")
root.geometry("450x500")


tk.Label(root, text="Name").pack(pady=5)
name_entry = tk.Entry(root, width=35)
name_entry.pack()

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root, width=35)
email_entry.pack()

tk.Label(root, text="Gender").pack(pady=5)

gender_var = tk.StringVar()

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Skills").pack(pady=5)

python_var = tk.IntVar()
sql_var = tk.IntVar()
excel_var = tk.IntVar()

tk.Checkbutton(root, text="Python", variable=python_var).pack()
tk.Checkbutton(root, text="SQL", variable=sql_var).pack()
tk.Checkbutton(root, text="Excel", variable=excel_var).pack()


tk.Label(root, text="Course").pack(pady=5)

course_var = tk.StringVar()
course_var.set("Select Course")

courses = ["Python", "Data Analytics", "Data Science", "Web Development"]

dropdown = ttk.Combobox(root, textvariable=course_var, values=courses)
dropdown.pack()

tk.Button(root, text="Submit", command=submit, bg="green", fg="white").pack(pady=20)

root.mainloop()
