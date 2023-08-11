

# for i in range(0,10):
#     if i == 3 or i== 5 or i == 7:
#         continue
# print(i)
#=================================
lista = [1,2,3]
# for i in range (10):
#     if i in lista:
#         print(i)
#
# zbir  = 0
# brojac = 0
# for i in lista:
#     if i == lista[0] or i == lista[len(lista)-1]:
#         continue
#     zbir += i
#
# print(zbir)
# zbir = 0
# for unos in range(3):
#     korisnik = int(input("Unesite broj:"))
#     zbir += korisnik
#     print(zbir)


# pitati korisnika da unese 5 br svaki od tih br dodati u listu na kraju printovatu poslednji br u listu
# lista = []
# for i in range(5):
#     korisnik = int(input("Unesite broj:"))
#     if korisnik %2==0:
#         continue
#     lista.append(korisnik)
#
# print(lista[len(lista)-2])

fajl = open("file.txt","r",encoding="utf-8")

podaciUFajlu = fajl.readlines()
zbir = 0
for i in podaciUFajlu:
    try:
        int(i)
    except Exception:
        break
    zbir+= int(i)
    print(zbir)




fajl.close()





