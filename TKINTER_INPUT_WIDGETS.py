# Ethan Gueck
# Practice with Tkinter input widgets

import tkinter
from tkinter import *
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
var = StringVar()
var.set("one")
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=60, y=150)

lb = Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=250, y=150)

v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="male", variable=v0, value=1)
r2 = Radiobutton(window, text="female", variable=v0, value=2)
r1.place(x=100, y=50)
r2.place(x=180, y=50)

v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text="Cricket", variable=v1)
C2 = Checkbutton(window, text="Tennis", variable=v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)


var = StringVar(window)
var.set("Check")
w = OptionMenu(window, variable = var, value="options:")
w.pack()
first = BooleanVar()
second = BooleanVar()
third = BooleanVar()
w['menu'].add_checkbutton(label="First", onvalue=True,
                          offvalue=False, variable=first)
w['menu'].add_checkbutton(label="Second", onvalue=True,
                          offvalue=False, variable=second)
w['menu'].add_checkbutton(label="Third", onvalue=1,
                          offvalue=False, variable=third)


wb = window.bind('<Button-3>', lambda x: print("First:", first.get(), " Second:",
           second.get(), " - Third:", third.get()))




menubar = tkinter.Menu(window)
show_all = tkinter.BooleanVar()
show_all.set(True)
show_done = tkinter.BooleanVar()
show_not_done = tkinter.BooleanVar()

view_menu = tkinter.Menu(menubar)
view_menu.add_checkbutton(label="Show All", onvalue=1, offvalue=0, variable=show_all)
view_menu.add_checkbutton(label="Show Done", onvalue=1, offvalue=0, variable=show_done)
view_menu.add_checkbutton(label="Show Not Done", onvalue=1, offvalue=0, variable=show_not_done)
menubar.add_cascade(label='View', menu=view_menu)
window.config(menu=menubar)

button = tkinter.Button(window, text='Button', command=lambda: print(wb.__getitem__()))
button.place(x=180, y=190)

window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()