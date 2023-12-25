people = [
    {"name": "Yunisha", "Surname": "Regmi"},
    {"name": "Sapana", "Surname": "Gartaula"},
    {"name": "Sumina", "Surname": "Neupane"},
    {"name": "Sarita", "Surname": "Bhattari"}
]


people.sort(key=lambda person: person["name"])
print(people)