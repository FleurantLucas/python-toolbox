import tkinter as tk
from tkinter import ttk
import datetime


class TimeTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text="", font=("Arial", 16))
        self.label.pack(pady=20)

        ttk.Button(self, text="Get Time", command=self.update_time).pack()

    def update_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.label.config(text=now)
