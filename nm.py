# This is text editor where i have added few more features like increasing and decreasing fonts ,Bold and italic feature.

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", ".txt")])

    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", ".txt")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully")

def toggle_bold():
    current_font = text["font"]
    font_family, font_size, font_style = current_font.split()
    
    if "bold" in font_style:
        new_font = f"{font_family} {font_size} normal"
    else:
        new_font = f"{font_family} {font_size} bold"
    
    text.config(font=new_font)

def toggle_italic():
    current_font = text["font"]
    font_family, font_size, font_style = current_font.split()
    
    if "italic" in font_style:
        new_font = f"{font_family} {font_size} normal"
    else:
        new_font = f"{font_family} {font_size} italic"
    
    text.config(font=new_font)    

def increase_font_size():
    current_font = text["font"]
    font_family, font_size, font_style = current_font.split()
    new_size = int(font_size) + 2  # Increase size by 2
    new_font = f"{font_family} {new_size} {font_style}"
    text.config(font=new_font)

def decrease_font_size():
    current_font = text["font"]
    font_family, font_size, font_style = current_font.split()
    new_size = max(8, int(font_size) - 2)  # Decrease size by 2, but minimum is 8
    new_font = f"{font_family} {new_size} {font_style}"
    text.config(font=new_font)

# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Add File menu
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Format menu
format_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Bold", command=toggle_bold)
format_menu.add_command(label="Italic", command=toggle_italic)
format_menu.add_command(label="Increase Font Size", command=increase_font_size)
format_menu.add_command(label="Decrease Font Size", command=decrease_font_size)

# Create a text widget with default font
default_font = "Helvetica 12 normal"
text = tk.Text(root, wrap=tk.WORD, font=default_font, fg="black")
text.pack(expand=tk.YES, fill=tk.BOTH)

# Create a text widget
#text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")
#text.pack(expand=tk.YES, fill=tk.BOTH)

# Run the application
root.mainloop()
