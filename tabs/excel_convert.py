import tkinter as tk
from tkinter import ttk


def excel_col_to_number(col):
    col = col.upper()
    result = 0

    for char in col:
        if not char.isalpha():
            raise ValueError("Invalid column")

        result = result * 26 + (ord(char) - ord('A') + 1)

    return result - 1  # zero-based


class ExcelColumnTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(
            self,
            text="Excel Column → Number",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        input_frame = ttk.Frame(self)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Column:").grid(row=0, column=0, padx=5)

        self.entry = ttk.Entry(input_frame, width=10)
        self.entry.grid(row=0, column=1, padx=5)
        self.entry.focus()

        ttk.Button(
            input_frame,
            text="Convert",
            command=self.convert
        ).grid(row=0, column=2, padx=5)

        self.result_label = ttk.Label(
            self,
            text="Result: —",
            font=("Segoe UI", 12)
        )
        self.result_label.pack(pady=10)

        # Press Enter to convert
        self.entry.bind("<Return>", lambda e: self.convert())

    def convert(self):
        col = self.entry.get().strip()

        if not col:
            return

        try:
            number = excel_col_to_number(col)
            self.result_label.config(text=f"Result: {number}")
        except ValueError:
            self.result_label.config(text="Invalid column")
