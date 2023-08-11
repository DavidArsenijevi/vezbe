indeks = input("unesite broj indeksa:").upper()
godinaupisa = "20" + indeks[2:4]
print("godina upisa:",godinaupisa)
if int(godinaupisa)>=2006 and int(godinaupisa)<2009:
    print("akreditacija 2006")
elif int(godinaupisa)>=2009 and int(godinaupisa)<2014:
    print("akreditacija 2009")
elif int(godinaupisa)>=2014 and int(godinaupisa)<2020:
    print("akreditacija 2014")
modul = indeks[:2]

if modul == "TS":
    print("modul:TK saobr i mreze")
if modul == "PS":
    print("postanski saobr i mreze")
if modul == "LO":
    print("logistika")
if modul == "VZ":
    print("vazdusni saobr i transport")
if modul == "VD":
    print("vodni saobr i transport")
if modul == "DB":
    print("bezbednost dr saobr")
if modul == "DT":
    print("drumski gradski transport")
if modul == "DS":
    print("drumski i gradski saobr")
if modul == "ZE":
    print("Zeleznicki saobracajni transport")
