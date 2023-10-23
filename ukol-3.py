import json

with open("body.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

hodnoceni = {}

for student, hodnota in data.items():
    if hodnota >= 60:
        hodnota = "Pass"
    else:
        hodnota = "Fail"
    if hodnota not in  hodnoceni:
        hodnoceni[student] = hodnota
print(hodnoceni)

with open("prospech.json", mode="w", encoding="utf-8") as output_file:
    json.dump(hodnoceni, output_file, indent=4, ensure_ascii=False)

"""
Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). 
Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", 
pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".
"""