izbor = input("odaberite sta zelite da pretvarate:\n\ta - celzijusi u faranhajte\n\te - faranhajte u celzijuse\n").lower()

if izbor == "a":
    celzijusi = float(input("unesite temperaturu u celzijusima:"))
    farenhajti = 1.8*celzijusi+32
    print("temperatura u celzijusima",celzijusi)
    print("temperatura u farenhajtima", farenhajti)

elif izbor == "e":
    farenhajti = float(input("unesite temperaturu u farenhajtima:"))
    celzijusi = (farenhajti-32)/1.8
    print("temperatura u farenhajtima", farenhajti)
    print("temperatura u celzijusima", celzijusi)



else:
    print("uneli ste pogresno slovo")
