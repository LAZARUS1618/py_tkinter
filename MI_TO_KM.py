# Ethan Gueck
# This is a small tkinter application that will convert miles to kilometers.
# Credit to Free Code Camp tkinter tutorials!

import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

# Create window
class Window:
    def __init__(self, master):
        self.master = master

    def add_items(self):
        self.entry_int = tk.IntVar()
        self.output_string = tk.StringVar()

        self.title_label = ttk.Label(master=self.master, text='Miles to kilomoters', font='Calibri 24')
        self.title_label.pack()

        self.frame = ttk.Frame(master=self.master)
        self.input_frame = ttk.Frame(master=self.frame)

        self.entry = ttk.Entry(master=self.input_frame, textvariable=self.entry_int)
        self.button = ttk.Button(master=self.input_frame, text='convert', command=self.convert)
        self.output = ttk.Label(master=self.frame, text='Output', font='Calibri 24', textvariable=self.output_string)
        self.frame.pack()
        self.input_frame.pack(pady=10)
        self.entry.pack(side='left', padx=10)
        self.button.pack(side='left')
        self.output.pack()
        return(self.frame, self.entry, self.button)

    def convert(self):
        try:
            self.output = self.entry_int.get()
            self.output = self.output * 1.60934
            self.output = str(self.output)
            self.output_string.set(self.output)
        except:
            self.output_string.set('Invalid Input')

window = ttk.Window(themename='darkly')#'superhero'
window.title = ('Calculator')
window.geometry('300x150')
window_items = Window(window)
window_items.add_items()
tk.mainloop()