from tkinter import *
from tkinter import messagebox
root=Tk()

root.geometry("200x300")
def MSG():
    messagebox.askquestion("Title","YOU HAVE GOT A VIRUS IN YOUR COMPUTER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

b1=Button(text="file", command=MSG)
b1.pack()

root.mainloop()
    

