import tkinter as tk
from bindings import *

MAX_POINTS = 30
Stats = {
    "Body": [0,
             {
                 "Strength": [0, {"Tone": 0, "Endurance": 0}],
                 "Dexterity": [0, {"Agility": 0, "Speed": 0}],
                 "Constitution": [0, {"Resolve": 0, "Bulk": 0}]
             }],
    "Mind": [0,
             {
                 "Intelligence": [0, {"Recall": 0, "Deduction": 0}],
                 "Wisdom": [0, {"Understanding": 0, "Faith": 0}],
                 "Charisma": [0, {"Urge": 0, "Instinct": 0}]
             }]
}


# 1              2              3
class Character:

    def build_control_list(self): # This makes us have an easy to manipulate list.
        # core_holder = {}
        dev_holder = {}
        for stat in Stats.values():
            for stat2 in stat[1].values():
                for (key, value) in zip(stat2[1].keys(), stat2[1].values()):
                    dev_holder.update({key: value})
        return dev_holder

    def __init__(self):
        self.Stats = self.build_control_list()
        self.MAX_POINTS = MAX_POINTS
        self.Spent_Points = 0

    def load(self, data):
        self.Stats = data

    def check(self):
        spent = sum(self.Stats.values())
        return spent == self.MAX_POINTS


class Interface:
    def body_and_mind_scale_action(self, value=None):
        self.body_display.configure(text=str(self.body_and_mind_scale.get()))
        self.mind_display.configure(text=str(MAX_POINTS - self.body_and_mind_scale.get()))

    def event_connection(self):
        self.body_and_mind_scale.bind('<B1-Motion>', self.body_and_mind_scale_action)

    def __init__(self):  # menu, body_display, body_and_mind_scale, mind_display
        self.menu = tk.Tk()
        self.body_display = tk.Label(self.menu, text=0)
        self.mind_display = tk.Label(self.menu, text=0)
        self.body_and_mind_scale = tk.Scale(self.menu, from_=6, to=24, orient=tk.HORIZONTAL, showvalue=False)
        self.name = tk.Entry(self.menu)
        self.army = tk.Entry(self.menu)

        self.menu.title('Quest')
        # Making a Window
        tk.Label(self.menu, text='Name: ').grid(row=0)
        tk.Label(self.menu, text='Army Name: ').grid(row=1)
        tk.Label(self.menu, text='Body').grid(row=2)
        self.body_display.grid(row=3)
        self.body_and_mind_scale.grid(row=2, column=1)
        tk.Label(self.menu, text='Mind').grid(row=2, column=2)
        self.mind_display.grid(row=3, column=2)
        self.name.grid(row=0, column=1)
        self.army.grid(row=1, column=1)
        self.event_connection()
