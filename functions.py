MAX_POINTS = 30
Stats = {
    "Body": [6,
             {
                 "Strength": [2, {"Tone": 1, "Endurance": 1}],
                 "Dexterity": [2, {"Agility": 1, "Speed": 1}],
                 "Constitution": [2, {"Resolve": 1, "Bulk": 1}]
             }],
    "Mind": [6,
             {
                 "Intelligence": [2, {"Recall": 1, "Deduction": 1}],
                 "Wisdom": [2, {"Understanding": 1, "Faith": 1}],
                 "Charisma": [2, {"Urge": 1, "Instinct": 1}]
             }]
}
# 1              2              3
Base_Stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
Sub_Stats = {
    "Tone": 1, "Endurance": 1,
    "Agility": 1, "Speed": 1,
    "Resolve": 1, "Bulk": 1,

    "Recall": 1, "Deduction": 1,
    "Understanding": 1, "Faith": 1,
    "Urge": 1, "Instinct": 1
}

Army_Numbers = {
    "Infantry": 0,
    "Beast": 0,
    "Heavy": 0,
    "Healer": 0,
    "Casters": 0,
    "Artillery": 0,
    "Fortifications": 0
}

Army_Calculation = {
    "Infantry": ["Endurance", "Speed", "Resolve"],
    "Beast": ["Understanding", "Instinct", "Deduction"],
    "Heavy": ["Bulk", "Tone", "Urge"],
    "Healer": ["Faith", "Endurance", "Agility"],
    "Casters": ["Recall", "Resolve", "Urge"],
    "Artillery": ["Bulk", "Deduction", "Endurance"],
    "Fortifications": ["Resolve", "Recall", "Tone"]
}


def build_control_list(data=None):  # This makes us have an easy to manipulate list.
    # core_holder = {}
    if data is None:
        data = Stats
    dev_holder = {}
    for stat in data.values():
        for stat2 in stat[1].values():
            for (key, value) in zip(stat2[1].keys(), stat2[1].values()):
                dev_holder.update({key: value})
    return dev_holder





