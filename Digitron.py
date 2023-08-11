print("unesite redni broj operacije")
print("1) sabiranje")
print("2) oduzimanje")
print("3) mnozenje")
print("4) deljenje")



if unos == "1" or unos == "2" or unos == "3" or unos == "4":
    broj1 = input("unesi broj1: ")
    broj2 = input("unesi broj2: ")
    broj3 = input("unesi broj3: ")


    if broj1.isdigit():
        broj1 = float(broj1)
    else:
        print("pogledaj se saberi se")
        exit()


    if broj2.isdigit():
        broj2 = float(broj2)
    else :
        print("nije dobro brate saberi se")
        exit()


    if broj3.isdigit():
        broj3 = float(broj3)
    else :
        print("nije dobro brate saberi se")
        exit()


    if unos == "1":
        zbir = broj1 + broj2 + broj3
        print("Zbir je :",zbir)
    if unos == "2":
        razlika = broj1 - broj2 - broj3
        print("Razlika je :",razlika)
    if unos == "3":
        proizvod = broj1 * broj2 * broj3
        print("Proizvod je :",proizvod)
    if unos == "4":
        kolicnik = broj1 / broj2 / broj3
        print("Kolicnik je :",kolicnik)

else :
    print("e brate nisi uneo broj od 1 do 4")
