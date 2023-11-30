# Ethan Gueck
# This app is intended to be a tkinter template for my other applications.

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("My App")
        self.style = Style(theme='darkly')

        self.header_frame = HeaderFrame(self.master)
        self.body_frame = BodyFrame(self.master)
        self.footer_frame = FooterFrame(self.master)

        self.notebook = ttk.Notebook(self.body_frame)
        self.tab1 = TabContentFrame(self.notebook, text="Tab 1")
        self.tab2 = TabContentFrame(self.notebook, text="Tab 2")
        self.tab3 = TabContentFrame(self.notebook, text="Tab 3")
        self.notebook.add(self.tab1, text="Tab 1")
        self.notebook.add(self.tab2, text="Tab 2")
        self.notebook.add(self.tab3, text="Tab 3")
        self.notebook.pack(fill="both", expand=True)
class TabContentFrame(tk.Frame):
    def __init__(self, parent, text):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.text = text
        self.widgets = None

        self.parent.bind("<<NotebookTabChanged>>", self.on_tab_changed)
    def on_tab_changed(self, event):
        if self.parent.select() == self:
            self.load_widgets()
    def load_widgets(self):
        if self.widgets is None:
            if self.text == "Tab 1":
                self.widgets = Add_Widgets_Tab1(self)
            elif self.text == "Tab 2":
                self.widgets = Add_Widgets_Tab2(self)
            elif self.text == "Tab 3":
                self.widgets = Add_Widgets_Tab3(self)

        # Add widgets to the tab
        self.widgets.pack(fill="both", expand=True)
class Add_Widgets_Tab1(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        label1 = ttk.Label(self, text="Label 1")
        label1.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Button 1")
        button1.pack(padx=10, pady=10)
class Add_Widgets_Tab2(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        label2 = ttk.Label(self, text="Label 2")
        label2.pack(padx=10, pady=10)

        button2 = ttk.Button(self, text="Button 2")
        button2.pack(padx=10, pady=10)
class Add_Widgets_Tab3(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        label3 = ttk.Label(self, text="Label 3")
        label3.pack(padx=10, pady=10)

        button3 = ttk.Button(self, text="Button 3")
        button3.pack(padx=10, pady=10)
class HeaderFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=100, borderwidth=2, relief="ridge")
        self.pack(side="top", fill="x")
        tk.Label(self, text="Header", font=("Arial", 16), bg="#333", fg="#fff").pack(pady=10)
class BodyFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth=2, relief="groove", width=800, height=450)
        self.pack(side="top", fill="both", expand=True)
class FooterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=50, borderwidth=2, relief="ridge")
        self.pack(side="bottom", fill="x")
        tk.Label(self, text="Footer", font=("Arial", 16), bg="#333", fg="#fff").pack(pady=10)


root = ttk.Window()
app = MyApp(root)
root.mainloop()