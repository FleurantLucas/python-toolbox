import tkinter as tk
from tkinter import ttk

# Import tab classes
from tabs.time_tab import TimeTab


class ToolboxApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lucas' Toolbox")
        self.geometry("500x350")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Add tabs
        notebook.add(TimeTab(notebook), text="Time")
        # notebook.add(RandomTab(notebook), text="Random")
        # notebook.add(NotesTab(notebook), text="Notes")


if __name__ == "__main__":
    app = ToolboxApp()
    app.mainloop()
