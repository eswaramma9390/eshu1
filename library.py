import tkinter as tk
from tkinter import messagebox, filedialog
import openpyxl
from openpyxl.styles import Font

class BookEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Book Entry")
        self.root.geometry("500x400")

        self.books = []

        tk.Label(root, text="Title:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Author:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.author_entry = tk.Entry(root, width=40)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="ISBN:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.isbn_entry = tk.Entry(root, width=40)
        self.isbn_entry.grid(row=2, column=1, padx=5, pady=5)

        add_btn = tk.Button(root, text="Add Book", command=self.add_book)
        add_btn.grid(row=3, column=0, columnspan=2, pady=10)

        self.listbox = tk.Listbox(root, width=60, height=10)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        save_btn = tk.Button(root, text="Save to Excel", command=self.save_to_excel)
        save_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        isbn = self.isbn_entry.get().strip()

        if not title or not author or not isbn:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        book_str = f"Title: {title} | Author: {author} | ISBN: {isbn}"
        self.books.append((title, author, isbn))
        self.listbox.insert(tk.END, book_str)

        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)

    def save_to_excel(self):
        if not self.books:
            messagebox.showwarning("No Data", "No books to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx")],
                                                 title="Save books as")
        if not file_path:
            return

        try:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Books"

            headers = ["Title", "Author", "ISBN"]
            ws.append(headers)
            for col_num, header in enumerate(headers, 1):
                cell = ws.cell(row=1, column=col_num)
                cell.font = Font(bold=True)

            for book in self.books:
                ws.append(book)

            wb.save(file_path)
            messagebox.showinfo("Success", f"Books saved to {file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookEntryApp(root)
    root.mainloop()
