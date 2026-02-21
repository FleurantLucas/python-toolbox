import tkinter as tk
from tkinter import ttk

# Import tab classes
from tabs.time_tab import TimeTab
from tabs.excel_convert import ExcelColumnTab
from tabs.pokemon_type_chart import PokemonTypeTab


class ToolboxApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lucas' Toolbox")
        self.geometry("800x500")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Add tabs
        notebook.add(TimeTab(notebook), text="Time")
        notebook.add(ExcelColumnTab(notebook), text="Excel Cols")
        notebook.add(PokemonTypeTab(notebook), text="Pokémon Type")
        # notebook.add(RandomTab(notebook), text="Random")
        # notebook.add(NotesTab(notebook), text="Notes")


if __name__ == "__main__":
    app = ToolboxApp()
    app.mainloop()
