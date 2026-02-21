import tkinter as tk
from tkinter import ttk

# ---------- Types ----------
TYPES = [
    "Normal","Fire","Water","Electric","Grass","Ice",
    "Fighting","Poison","Ground","Flying","Psychic",
    "Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"
]

TYPE_COLORS = {
    "Normal": "#A8A77A", "Fire": "#EE8130", "Water": "#6390F0",
    "Electric": "#F7D02C", "Grass": "#7AC74C", "Ice": "#96D9D6",
    "Fighting": "#C22E28", "Poison": "#A33EA1", "Ground": "#E2BF65",
    "Flying": "#A98FF3", "Psychic": "#F95587", "Bug": "#A6B91A",
    "Rock": "#B6A136", "Ghost": "#735797", "Dragon": "#6F35FC",
    "Dark": "#705746", "Steel": "#B7B7CE", "Fairy": "#D685AD",
}

# ---------- Defensive chart ----------
TYPE_CHART = {
    "Normal": {"Fighting": 2, "Ghost": 0},
    "Fire": {"Water": 2, "Ground": 2, "Rock": 2,
             "Fire": .5, "Grass": .5, "Ice": .5, "Bug": .5, "Steel": .5, "Fairy": .5},
    "Water": {"Electric": 2, "Grass": 2,
              "Fire": .5, "Water": .5, "Ice": .5, "Steel": .5},
    "Electric": {"Ground": 2,
                 "Electric": .5, "Flying": .5, "Steel": .5},
    "Grass": {"Fire": 2, "Ice": 2, "Poison": 2, "Flying": 2, "Bug": 2,
              "Water": .5, "Electric": .5, "Grass": .5, "Ground": .5},
    "Ice": {"Fire": 2, "Fighting": 2, "Rock": 2, "Steel": 2,
            "Ice": .5},
    "Fighting": {"Flying": 2, "Psychic": 2, "Fairy": 2,
                 "Bug": .5, "Rock": .5, "Dark": .5},
    "Poison": {"Ground": 2, "Psychic": 2,
               "Grass": .5, "Fighting": .5, "Poison": .5,
               "Bug": .5, "Fairy": .5},
    "Ground": {"Water": 2, "Grass": 2, "Ice": 2,
               "Poison": .5, "Rock": .5, "Electric": 0},
    "Flying": {"Electric": 2, "Ice": 2, "Rock": 2,
               "Grass": .5, "Fighting": .5, "Bug": .5,
               "Ground": 0},
    "Psychic": {"Bug": 2, "Ghost": 2, "Dark": 2,
                "Fighting": .5, "Psychic": .5},
    "Bug": {"Fire": 2, "Flying": 2, "Rock": 2,
            "Grass": .5, "Fighting": .5, "Ground": .5},
    "Rock": {"Water": 2, "Grass": 2, "Fighting": 2,
             "Ground": 2, "Steel": 2,
             "Normal": .5, "Fire": .5, "Poison": .5, "Flying": .5},
    "Ghost": {"Ghost": 2, "Dark": 2,
              "Poison": .5, "Bug": .5,
              "Normal": 0, "Fighting": 0},
    "Dragon": {"Ice": 2, "Dragon": 2, "Fairy": 2,
               "Fire": .5, "Water": .5, "Electric": .5, "Grass": .5},
    "Dark": {"Fighting": 2, "Bug": 2, "Fairy": 2,
             "Ghost": .5, "Dark": .5,
             "Psychic": 0},
    "Steel": {"Fire": 2, "Fighting": 2, "Ground": 2,
              "Normal": .5, "Grass": .5, "Ice": .5,
              "Flying": .5, "Psychic": .5, "Bug": .5,
              "Rock": .5, "Dragon": .5, "Steel": .5,
              "Fairy": .5, "Poison": 0},
    "Fairy": {"Poison": 2, "Steel": 2,
              "Fighting": .5, "Bug": .5, "Dark": .5,
              "Dragon": 0}
}


# ---------- Fancy Rounded Button ----------
class TypeButton(tk.Canvas):
    def __init__(self, parent, text, color, command):
        super().__init__(parent, width=110, height=32,
                         highlightthickness=0, bg=parent["bg"])

        self.text = text
        self.color = color
        self.command = command
        self.selected = False

        self.draw(color)

        self.bind("<Button-1>", self.click)
        self.bind("<Enter>", self.hover)
        self.bind("<Leave>", self.unhover)

    def draw(self, color, outline="", width=0):
        self.delete("all")

        w = int(self["width"])
        h = int(self["height"])

        self.create_rectangle(
            width//2, width//2,
            w - width//2, h - width//2,
            fill=color,
            outline=outline,
            width=width
        )

        self.create_text(
            w//2,
            h//2,
            text=self.text,
            fill="black",
            font=("Segoe UI", 9, "bold")
        )

    def click(self, _):
        self.command(self.text)

    def hover(self, _):
        if not self.selected:
            self.draw(self.color, outline="black", width=3)

    def unhover(self, _):
        if not self.selected:
            self.draw(self.color, outline="", width=0)

    def set_selected(self, value):
        self.selected = value

        if value:
            self.draw(self.color, outline="black", width=3)
        else:
            self.draw(self.color, outline="", width=0)

# ---------- Main Tab ----------
class PokemonTypeTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_type1 = None
        self.selected_type2 = None

        ttk.Label(self, text="Pokémon Type Effectiveness",
                  font=("Segoe UI", 15, "bold")).pack(pady=8)

        self.build_type_section("Type 1", is_type1=True)
        self.build_type_section("Type 2 (optional)", is_type1=False)

        self.result_frame = tk.Frame(self)
        self.result_frame.pack(pady=10, fill="x")

    # ---------- UI Builders ----------
    def build_type_section(self, title, is_type1):
        ttk.Label(self, text=title,
                  font=("Segoe UI", 12, "bold")).pack(pady=(10, 2))

        frame = tk.Frame(self)
        frame.pack()

        buttons = {}

        for i, t in enumerate(TYPES):
            btn = TypeButton(
                frame,
                t,
                TYPE_COLORS[t],
                lambda typ=t, t1=is_type1: self.select_type(typ, t1)
            )

            btn.grid(row=i // 6, column=i % 6, padx=3, pady=3)
            buttons[t] = btn

        if is_type1:
            self.type1_buttons = buttons
        else:
            self.type2_buttons = buttons

    # ---------- Selection ----------
    def select_type(self, typ, is_type1):
        if is_type1:
            self.selected_type1 = typ
            self.update_buttons(self.type1_buttons, typ)
        else:
            self.selected_type2 = None if self.selected_type2 == typ else typ
            self.update_buttons(self.type2_buttons, self.selected_type2)

        self.update_results()

    def update_buttons(self, btns, selected):
        for t, b in btns.items():
            b.set_selected(t == selected)

    # ---------- Calculation ----------
    def update_results(self):
        for w in self.result_frame.winfo_children():
            w.destroy()

        t1 = self.selected_type1
        t2 = self.selected_type2

        if not t1:
            return

        multipliers = {}

        for atk in TYPES:
            m = TYPE_CHART.get(t1, {}).get(atk, 1)
            if t2:
                m *= TYPE_CHART.get(t2, {}).get(atk, 1)
            multipliers[atk] = m

        self.show_group("4× Weak", multipliers, lambda m: m >= 4)
        self.show_group("2× Weak", multipliers, lambda m: 2 <= m < 4)
        self.show_group("Resists", multipliers, lambda m: 0 < m < 1)
        self.show_group("Immune", multipliers, lambda m: m == 0)

    # ---------- Result Display ----------
    def show_group(self, title, data, condition):
        items = [t for t, m in data.items() if condition(m)]
        if not items:
            return

        ttk.Label(self.result_frame, text=title,
                  font=("Segoe UI", 11, "bold")).pack(anchor="w")

        row = tk.Frame(self.result_frame)
        row.pack(anchor="w", pady=2)

        for t in items:
            tk.Label(
                row,
                text=t,
                bg=TYPE_COLORS[t],
                fg="white",
                padx=6,
                pady=2,
                font=("Segoe UI", 9, "bold")
            ).pack(side="left", padx=2)