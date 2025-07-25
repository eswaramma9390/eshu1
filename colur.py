import tkinter as tk
from tkinter import messagebox
import csv
import os

def submit_data():
    data = entry.get().strip()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    file_exists = os.path.isfile("data.csv")
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Input Data"])  # Write header only once
        writer.writerow([data])

    messagebox.showinfo("Success", f"Data saved: {data}")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Save Data to CSV")

tk.Label(root, text="Enter some data:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

submit_btn = tk.Button(root, text="Submit & Save to CSV", command=submit_data)
submit_btn.pack(pady=20)

root.mainloop()
