budzet = input(("unesi budzet"))
if budzet.isdigit():
    cenaPiva = input("unesi cenu piva")
    if cenaPiva.isdigit():
        budzet = float(budzet)
        cenaPiva = float(cenaPiva)
        kolicina = budzet / cenaPiva
        print("ukupno  mozete da kupite",kolicina)
    else :
        print("drugi broj nije broj")

else :
    print("Prvi broj nije broj")

#
# if budzet.isdigit() and cenaPiva.isdigit() :
#
# else :
#     print("Neki broj koji ste uneli nije broj")
