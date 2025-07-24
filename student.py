import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # pip install tkcalendar
import csv
import os

CSV_FILE = "attendance.csv"
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

def mark_attendance(status):
    selected_date = date_entry.get()
    student_name = student_var.get()
    
    if not student_name:
        messagebox.showwarning("Input Error", "Please select a student.")
        return

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Student Name", "Attendance"])
        writer.writerow([selected_date, student_name, status])
    
    messagebox.showinfo("Success", f"{student_name} marked as {status} on {selected_date}")
    
    # Clear student selection after submission
    student_var.set('')
    # Optionally reset date to today (uncomment if desired)
    # date_entry.set_date(date_entry._date.today())

# Main window setup
root = tk.Tk()
root.title("Student Attendance Tracker")
root.geometry("400x300")

# Date label and calendar picker
tk.Label(root, text="Select Date:").pack(pady=5)
date_entry = DateEntry(root, width=20, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
date_entry.pack(pady=5)

# Student label and dropdown
tk.Label(root, text="Select Student:").pack(pady=5)
student_var = tk.StringVar()
student_dropdown = ttk.Combobox(root, textvariable=student_var, values=students, state='readonly')
student_dropdown.pack(pady=5)

# Buttons for attendance marking
tk.Button(root, text="Mark Present", width=15, bg="green", fg="white",
          command=lambda: mark_attendance("Present")).pack(pady=10)

tk.Button(root, text="Mark Absent", width=15, bg="red", fg="white",
          command=lambda: mark_attendance("Absent")).pack()

root.mainloop()
