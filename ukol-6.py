class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if self.dostupne == False:
            return "Vozidlo není k dispozici."
        else:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla."
        
    def get_info(self):
        return f"Auto {self.typ_vozidla}, které si chcete půjčit, má registrační značku {self.registracni_znacka}."


Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253, True)

pujceni_auta = input("Jaké auto si přejete půjčit? (Peugeot nebo Skoda) ")

if pujceni_auta == "Peugeot":
    print(Peugeot.get_info())
    print(Peugeot.pujc_auto())
    print(Peugeot.pujc_auto())
else:
    print(Skoda.get_info())
    print(Skoda.pujc_auto())
    print(Skoda.pujc_auto())
    
"""
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka 	Značka a typ vozidla 	Počet najetých kilometrů
4A2 3020 	        Peugeot 403 Cabrio 	    47534
1P3 4747 	        Škoda Octavia 	        41253

Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. 
Třída bude mít tyto atributy:

   - registrační značka automobilu registracni_znacka,
   - značka a typ vozidla typ_vozidla,
   - počet najetých kilometrů najete_km,
   - informaci o tom, jestli je vozidlo aktuálně volné dostupne 
     (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).

Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla 
a počet kilometrů získej jako parametry funkce __init__ 
a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako True, 
tj. na začátku je vozidlo vždy volné.

Vytvoř objekty, které reprezentují oba automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) 
žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, 
změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text 
"Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text 
"Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle 
(stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel 
přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel 
vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij 
funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát.
"""