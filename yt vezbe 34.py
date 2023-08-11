mesta = ["Smederevo","Velika Plana","Smederevska Palanka","Kovin","Pozarevac","Kragujevac","Beograd","Pancevo","Vrsac"]
mesta.append("Kosovska Mitrovica")
#1. nacin for petlja
for i in mesta:
    print(i)
#2. nacin while
brojpodataka = len(mesta)
x = 0
while x<brojpodataka:
    print(mesta[x])
    x+=1
