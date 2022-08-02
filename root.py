# Multiple labels in one line using Tkinter
from tkinter import *

win = Tk()
win.title("Labels in One Line")
win.geometry("700x500")

label1=Label(win, text="Shahid ", font=("Times",30,"italic"), bg='red')
label1.pack(side=LEFT, pady=100,padx=150)

label2=Label(win, text="Asim", font=("Times",30,"italic"), bg='blue')
label2.pack(side=LEFT, pady=300,padx=450)

label3=Label(win, text="Hamza", font=("Times",30,"italic"), bg='green')
label3.pack(side=RIGHT, pady=100,padx=150)

win.mainloop()
