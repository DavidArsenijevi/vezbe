datum = input("Unesite datum u gramaticki ispravnom obliku:").rstrip(".")
podaci = datum.split(".")
print(podaci)
#1. meseci
meseci = [
    [1,"januar"],
    [2,"februar"],
    [3,"mart"],
    [4,"april"],
    [5,"maj"],
    [6,"jun"],
    [7,"jul"],
    [8,"avgust"],
    [9,"septembar"],
    [10,"oktobar"],
    [11,"novembar"],
    [12,"decembar"],
]
for i in range(12):
    if int(podaci[1])== meseci[i][0]:
        #print("Mesec:",meseci[i][1])
        print(f"Mesec: {meseci[i][1]}")
        break



#2. prestupna godina
if int(podaci[2])%400==0:
    print("Godina je prestupna")
elif int(podaci[2])%100!=0 and int(podaci[2])%4==0:
    print("Godina je prestupna")
else:
    print("Godina nije prestupna")
