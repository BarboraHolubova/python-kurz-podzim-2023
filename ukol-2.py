sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadej kód součástky: ")
mnozstvi = int(input("Zadej počet součástek: "))
if not kod in sklad:
    print("Součástka není skladem.")
elif mnozstvi > sklad[kod]:
    print(f"Součástky {kod} lze prodat pouze {sklad[kod]} kusů.")
    sklad.pop(kod)
    print(sklad)
else:
    print("Součástku lze prodat v plné výši.")
    sklad[kod] -= 50 
    print(sklad)