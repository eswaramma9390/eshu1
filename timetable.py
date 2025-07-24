import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import csv
import os

CSV_FILE = "study_log.csv"

def submit_log():
    subject = subject_var.get().strip()
    hours = hours_var.get().strip()
    date = date_entry.get()

    if not subject or not hours:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    try:
        hours_float = float(hours)
        if hours_float <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid positive number for hours.")
        return

    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Subject", "Hours Studied", "Date"])
        writer.writerow([subject, hours_float, date])

    messagebox.showinfo("Success", "Study session logged!")
    clear_fields()

def clear_fields():
    subject_var.set("")
    hours_var.set("")
    date_entry.set_date(date_entry._date.today())

root = tk.Tk()
root.title("Study Time Logger")
root.geometry("350x300")

subject_var = tk.StringVar()
hours_var = tk.StringVar()

tk.Label(root, text="Subject").pack(pady=5)
tk.Entry(root, textvariable=subject_var).pack()

tk.Label(root, text="Hours Studied").pack(pady=5)
tk.Entry(root, textvariable=hours_var).pack()

tk.Label(root, text="Date").pack(pady=5)
date_entry = DateEntry(root, width=18, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
date_entry.pack(pady=5)

tk.Button(root, text="Submit", command=submit_log, bg="blue", fg="white").pack(pady=15)

root.mainloop()
