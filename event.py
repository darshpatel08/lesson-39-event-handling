from tkinter import *
window=Tk()
window.title("CLICK ME")
window.geometry("200x300")

def key_press(event):
    print("the key that was pressed is ", event.char)
window.bind("<Key>", key_press)

def button_click(event):
    print("the button was clicked")
b1=Button(text="CLICK ME")
b1.pack()

b1.bind("<Button-1>", button_click)

window.mainloop()
