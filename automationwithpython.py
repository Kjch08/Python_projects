import tkinter as tk
from tkinter import Entry,Label,Button
import webbrowser

#Define main window

root=tk.Tk()
root.title("Your AI Assistant")

# Adding a background color
root.configure(bg="steelblue")

#Define the function to automate youtube search
def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

#Define the function to automate google search

def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

#Define the function to automate instagram search

def search_instagram():
    Username = new_func()
    url=f"https://www.instagram.com/{Username}/"
    webbrowser.open(url)

def new_func():
    Username=entry.get().replace('@',"")
    return Username

# Create input field,labels and buttons.
Label(root,text="Enter your command:").pack(pady=10)
entry=Entry(root,width=50)
entry.pack(pady=10)
Button(root,text="search on youtube",command=search_youtube).pack(pady=5)
Button(root,text="search on google",command=search_google).pack(pady=5)
Button(root,text="search on instagram",command=search_instagram).pack(pady=5)


# Run the GUI event loop
root.mainloop()


