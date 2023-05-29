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


# dev_stats =

class Character:

    def __init__(self):
        self.Stats = Stats
        self.MAX_POINTS = MAX_POINTS
        self.Spent_Points = 0

    def load(self, data):
        self.Stats = data

    def check(self):
        spent = 0
        for stat in Stats.values():
            for stat2 in stat[1].values():
                for stat3 in stat2[1].values():
                    spent = spent + stat3
        return spent == self.MAX_POINTS



