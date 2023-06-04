import tkinter as tk
from functions import *


class Character:
    def __init__(self):
        self.Stats = build_control_list()
        self.MAX_POINTS = MAX_POINTS
        self.Spent_Points = 12

    def load(self, data):
        self.Stats = build_control_list(data)

    def check(self):
        spent = sum(self.Stats.values())
        return spent == self.MAX_POINTS

    def set_value(self, stat, value):
        if self.Stats[stat] < value:
            self.Spent_Points = self.Spent_Points + 1
        elif self.Stats[stat] > value:
            self.Spent_Points = self.Spent_Points - 1
        self.Stats[stat] = value


class Interface(Character):
    def data_handler(self, mouse):
        print(self.Stats)

    def construct_spinbox(self, name=None, row=0, column=0):
        tk.Label(self.menu, text=name).grid(row=row, column=column)
        current_value = tk.StringVar(value='1')
        def value_changed(mouse=None):
            self.set_value(name, int(current_value.get()))
            self.point_spent.configure(text=f'Points:{self.Spent_Points}/{self.MAX_POINTS}')
            # spin_box.configure(to=self.MAX_POINTS - self.Spent_Points)

        spin_box = tk.Spinbox(self.menu,
                              from_=1,
                              to=self.MAX_POINTS - self.Spent_Points+1,
                              textvariable=current_value,
                              command=value_changed
                              )
        spin_box.grid(row=row, column=column + 1)
        spin_box.bind('<Enter>', value_changed)
        return spin_box

    def __init__(self):
        super().__init__()
        self.menu = tk.Tk()
        self.name = tk.Entry(self.menu)
        self.army = tk.Entry(self.menu)
        self.point_spent = tk.Label(self.menu, text=f'Points:{self.Spent_Points}/{self.MAX_POINTS}')

        self.menu.title('Quest')
        # Making a Window
        tk.Label(self.menu, text='Name: ').grid(row=0)
        tk.Label(self.menu, text='Army Name: ').grid(row=1)
        self.name.grid(row=0, column=1)
        self.army.grid(row=1, column=1)
        self.point_spent.grid(row=2, column=0)

        self.spinbox_list = []
        for index, name in enumerate(self.Stats.keys()):
            self.spinbox_list.append(self.construct_spinbox(name=name, row=index + 3))

        self.button = tk.Button(self.menu, text="Print Json")
        self.button.grid(row=16)
        self.button.bind('<Button-1>', self.data_handler)
