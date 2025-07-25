import tkinter as tk
import random

def change_bg_color():
    # Generate a random color in hex format
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    root.config(bg=random_color)

root = tk.Tk()
root.title("Random Background Color")

# Set initial window size
root.geometry("300x200")

# Create a button that calls change_bg_color when clicked
button = tk.Button(root, text="Change Color", command=change_bg_color)
button.pack(pady=50)

root.mainloop()
