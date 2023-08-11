def pravougaonik(a,b):
    Obim = 2*a+2*b
    Povrsina = a*b

    #print(f"o= {Obim}\np={Povrsina}")
    return Obim,Povrsina


#1nacin
"""
stranicaa = float(input("Unesite stranicu a:"))
stranicab = float(input("Unesite stranicu b:"))
pravougaonik(stranicaa,stranicab)
"""
#2nacin
stranice = []
stranice.append(float(input("Unesite stranicu a:")))
stranice.append(float(input("Unesite stranicu b:")))
obimpravougaonika,povrsinapravougaonika = pravougaonik(stranice[0],stranice[1])
print(f"O= {obimpravougaonika}")
print(f"P= {povrsinapravougaonika}")

