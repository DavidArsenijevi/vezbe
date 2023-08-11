imeiprezime = input("unesite ime i prezime:")
razmak = imeiprezime.find(" ")
#print(razmak)
ime = imeiprezime[0:razmak]
prezime = imeiprezime[razmak+1:]
inicijali = ime[0]+prezime[0]
print("Duzina imena:", len(ime))
print("Duzina prezimena", len(prezime))
print("inicijali", inicijali.upper())
