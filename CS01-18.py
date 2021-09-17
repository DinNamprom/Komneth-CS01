from tkinter import *

root = Tk()
root.title("First GUI")
Text1 = Label(text="My Name is",fg=("blue"),font=20).grid(row=0, column=0)
Text2 = Label(text="Komneth",fg=("red"),font=20).grid(row=1, column=1)
Text3 = Label(text="Namprom",fg=("green"),font=20).grid(row=2, column=2)
root.geometry("300x300")
root.mainloop()