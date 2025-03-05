<<<<<<< HEAD
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")

def time():
    string = strftime("%H:%M:%S %p \n %D")
    
    label.config(text = string)
    label.after(1000,time)

label = tk.Label(root,font= ('calibari',50,'bold'),background ='yellow',foreground ='black')
label.pack(anchor='center')


time()
=======
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")

def time():
    string = strftime("%H:%M:%S %p \n %D")
    
    label.config(text = string)
    label.after(1000,time)

label = tk.Label(root,font= ('calibari',50,'bold'),background ='yellow',foreground ='black')
label.pack(anchor='center')


time()
>>>>>>> 3353d59a9477253cefa40e096cc196cf85470aa3
root.mainloop()