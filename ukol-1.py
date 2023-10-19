jmeno = "Barbora"
print(f"{jmeno}@czechitas.cz")

jmeno_a_prijmeni = input("Zadej své celé jméno: ")
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
krestny, prijmeni = jmeno_a_prijmeni.split(" ")
print(f"{krestny[0].upper()}{krestny[1:].lower()} {prijmeni[0].upper()}{prijmeni[1:].lower()}")
print(f"{krestny[0].upper()}. {prijmeni[0].upper()}.")
delka_krestne = len(krestny)
if delka_krestne > 5: 
    print(f"{krestny[0].upper()}. {prijmeni[0].upper()}{prijmeni[1:].lower()}")
else:
    print(f"{krestny[0].upper()}{krestny[1:].lower()} {prijmeni[0].upper()}{prijmeni[1:].lower()}")