classes = [
    ("Paladin", "Protection", "Retribution", "Holy"),
    ("Warrior", "Protection", "Arms", "Fury"),
    ("Death Knight", "Blood", "Unholy", "Frost"),
]

wow_class = [item[0] for item in classes]
print(wow_class)
tanks = [spec[1] for spec in classes]
print(tanks)
dps = [spec[2] for spec in classes]
dps.append("Frost")
dps.append("Fury")
print(dps)
healing = ["Holy"]
print(healing)
print(f"""""")
