import tkinter as tk
from functions import *


class Character:
    def __init__(self):
        self.Stats = build_control_list()
        self.BaseStats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        self.CoreStats = ["Body", "Mind"]
        self.MAX_POINTS = MAX_POINTS
        self.Spent_Points = sum(self.Stats.values())

    def load(self, data):
        self.Stats = build_control_list(data)

    def check(self):
        spent = sum(self.Stats.values())
        return spent == self.MAX_POINTS


class Interface(Character):
    def data_handler(self, mouse):
        print(self.Stats)

    def count(self):
        self.Spent_Points = sum(self.Stats.values())
        indexer = 0
        for counter, values in enumerate(list(self.Stats.values())):
            if counter % 2 == 0:
                self.base_list[indexer]['text'] = sum([list(self.Stats.values())[counter], list(self.Stats.values())[counter+1]])
                indexer = indexer + 1
        self.core_list[0]['text'] = sum([x for c, x in enumerate(list(self.Stats.values())) if c < 6])
        self.core_list[1]['text'] = sum([x for c, x in enumerate(list(self.Stats.values())) if c > 5])

    def set_value(self, stat, value):
        self.Stats[stat] = value
        self.count()

    def construct_stats(self, name=None, row=0, column=0):
        tk.Label(self.menu, text=name, font=("Arial", 14)).grid(row=row, column=column)
        text = tk.Label(self.menu, text=0, font=("Arial", 14))
        text.grid(row=row + 1, column=column)
        return text

    def construct_spinbox(self, name=None, row=0, column=0):
        tk.Label(self.menu, text=name, font=("Arial", 14)).grid(row=row, column=column)
        current_value = tk.StringVar(value='1')

        def value_changed(mouse=None):
            current = int(current_value.get())
            # if current > int(spin_box['to']):
            #     spin_box['textvariable'] = str(int(spin_box['to']))
            #     current = int(spin_box['textvariable'])
            self.set_value(name, current)
            self.point_spent.configure(text=f'Points:{self.Spent_Points}/{self.MAX_POINTS}')

        spin_box = tk.Spinbox(self.menu,
                              from_=1,
                              to=self.MAX_POINTS,
                              textvariable=current_value,
                              command=value_changed,
                              font=("Arial", 14)
                              )
        spin_box.grid(row=row, column=column +1 , ipadx=5, ipady=5, pady=5, padx=5)
        spin_box.bind('<Return>', value_changed)
        spin_box.bind('<Enter>', value_changed)
        return spin_box

    def __init__(self):
        super().__init__()
        self.menu = tk.Tk()
        self.name = tk.Entry(self.menu, font=("Arial", 14))
        self.army = tk.Entry(self.menu, font=("Arial", 14))
        self.point_spent = tk.Label(self.menu,font=("Arial", 14), text=f'Points:{self.Spent_Points}/{self.MAX_POINTS}')

        self.menu.title('Quest')
        # Making a Window
        tk.Label(self.menu, text='Name: ', font=("Arial", 14)).grid(row=0)
        tk.Label(self.menu, text='Army Name: ', font=("Arial", 14)).grid(row=0, column=2)
        self.name.grid(row=0, column=1)
        self.army.grid(row=0, column=3)
        self.point_spent.grid(row=2, column=0)

        self.spinbox_list = []
        self.base_list = []
        self.core_list = []
        for index, name in enumerate(self.Stats.keys()):
            self.spinbox_list.append(self.construct_spinbox(name=name, row=index + 3, column=2))
        index_seperation = 0
        for name in self.BaseStats:
            self.base_list.append(self.construct_stats(name=name, row=index_seperation + 3, column=1))
            index_seperation = index_seperation + 2
        index_seperation = 0

        for name in self.CoreStats:
            self.core_list.append(self.construct_stats(name=name, row=index_seperation + 3, column=0))
            index_seperation = index_seperation + 6

        self.button = tk.Button(self.menu, text="Print Json")
        self.button.grid(row=16)
        self.button.bind('<Button-1>', self.data_handler)
