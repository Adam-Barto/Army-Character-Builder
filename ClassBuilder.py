import tkinter as tk
from functions import *


class Character:
    def __init__(self):
        self.Stats = build_control_list()
        self.MAX_POINTS = MAX_POINTS
        self.Spent_Points = 0

    def load(self, data):
        self.Stats = build_control_list(data)

    def check(self):
        spent = sum(self.Stats.values())
        return spent == self.MAX_POINTS

    def set(self, stat, value):
        self.Stats[stat] = value


class Interface(Character):
    def data_handler(self, mouse):
        print(self.Stats)

    def slider_action(self, value=None, items=None):
        if items is None:
            items = [self.body_display, self.mind_display, self.scale]
        items[0].configure(text=str(items[2].get()))
        items[1].configure(text=str(MAX_POINTS - items[2].get()))

    def construct_sliders(self, names_stats=None, row=0):
        if names_stats is None:
            names_stats = ["Error", "Found"]
        tk.Label(self.menu, text=names_stats[0]).grid(row=row)
        tk.Label(self.menu, text=names_stats[1]).grid(row=row, column=2)
        display_1 = tk.Label(self.menu, text=1)
        display_2 = tk.Label(self.menu, text=1)
        display_1.grid(row=(row + 1))
        display_2.grid(row=(row + 1), column=2)
        scale = tk.Scale(self.menu, from_=1, to=5, orient=tk.HORIZONTAL, showvalue=False)
        scale.grid(row=row, column=1)

        def binding(value=None):
            items = [display_1, display_2, scale]
            items[0].configure(text=str(items[2].get()))
            items[1].configure(text=str(6 - items[2].get()))
            self.set(names_stats[0], items[2].get())
            self.set(names_stats[1], items[2].get())

        scale.bind('<B1-Motion>', binding)

    def __init__(self):
        super().__init__()
        self.menu = tk.Tk()
        self.body_display = tk.Label(self.menu, text=1)
        self.mind_display = tk.Label(self.menu, text=24)
        self.scale = tk.Scale(self.menu, from_=6, to=24, orient=tk.HORIZONTAL, showvalue=False)
        self.name = tk.Entry(self.menu)
        self.army = tk.Entry(self.menu)

        self.menu.title('Quest')
        # Making a Window
        tk.Label(self.menu, text='Name: ').grid(row=0)
        tk.Label(self.menu, text='Army Name: ').grid(row=1)
        tk.Label(self.menu, text='Body').grid(row=2)
        tk.Label(self.menu, text='Mind').grid(row=2, column=2)
        self.body_display.grid(row=3)
        self.scale.grid(row=2, column=1)
        self.mind_display.grid(row=3, column=2)
        self.name.grid(row=0, column=1)
        self.army.grid(row=1, column=1)
        self.scale.bind('<B1-Motion>', self.slider_action)

        self.construct_sliders(names_stats=["Tone", "Endurance"], row=4)
        self.construct_sliders(names_stats=["Agility", "Speed"], row=6)
        self.construct_sliders(names_stats=["Resolve", "Bulk"], row=8)

        self.construct_sliders(names_stats=["Recall", "Deduction"], row=10)
        self.construct_sliders(names_stats=["Understanding", "Faith"], row=12)
        self.construct_sliders(names_stats=["Urge", "Instinct"], row=14)
        self.button = tk.Button(self.menu, text="Print Json")
        self.button.grid(row=16)
        self.button.bind('<Button-1>', self.data_handler)
