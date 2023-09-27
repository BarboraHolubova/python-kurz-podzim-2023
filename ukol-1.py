jmeno = "Barbora"
print(f"{jmeno}@czechitas.cz")

jmeno_a_prijmeni = input("Zadej své celé jméno: ")
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(jmeno_a_prijmeni)
krestny, prijmeni = jmeno_a_prijmeni.split(" ")
print(f"{krestny[0]}. {prijmeni[0]}.")
delka_krestne = len(krestny)
if delka_krestne > 5: 
    print(f"{krestny[0]} {prijmeni}")
else:
    print(jmeno_a_prijmeni)