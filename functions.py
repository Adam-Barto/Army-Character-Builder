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


def build_control_list(): # This makes us have an easy to manipulate list.
    # core_holder = {}
    dev_holder = {}
    for stat in Stats.values():
        for stat2 in stat[1].values():
            for (key, value) in zip(stat2[1].keys(), stat2[1].values()):
                dev_holder.update({key: value})
    return dev_holder
