import os
def provera_lozinke(lozinka):
    if len(lozinka) < 6:
        print("Šifra mora imati bar 6 karaktera")
        return False
    if not any(char.isdigit() for char in lozinka):
        print("Šifra mora sadržavati bar 1 broj.")
        return False
    if not any(char.isupper() for char in lozinka) and any(char.islower() for char in lozinka):
        print("Sifra mora da ima jedno veliko i jedno malo slovo. ")
        return  False

    return True


def uvodniMenu():
    while True:
        print("1)Kupac")
        print("2)Radnik")
        print("3)Kupac")
        print("4)Vlasnik")
        print("5)Admin")
        izaberiOpciju = int(input("Unesite zeljenu opciju: "))
        if izaberiOpciju == 1:
            break
        elif izaberiOpciju == 2:
            break
        elif izaberiOpciju == 3:
            break
        elif izaberiOpciju == 4:
            break
        elif izaberiOpciju == 5:
            break
        else:
            print("Uneli ste pogresnu opciju, probajte ponovo.\n")


def registracija():
    while True:

        email_Adresa = input("Unesite E-mail adresu: ")
        if email_Adresa.strip() == "":
            print("Email adresa ne sme biti prazna")
            continue


        lozinka = input("Unesite lozinku: ")
        if lozinka.strip() == "":
            print("Lozinka ne sme biti prazna")
        if not provera_lozinke(lozinka):
            continue


        ime = input("Unesite ime: ")
        if ime.strip() == "":
            print("Ime ne sme biti prazno")
            continue

        prezime = input("Unesite prezime: ")
        if prezime.strip() == "":
            print("Prezime ne sme biti prazno")
            continue

        adresa = input("Unesite adresu: ")
        if adresa.strip() == "":
            print("Adresa ne sme biti prazna")
            continue


def ocistiEkran():
    os.system['clear']



uvodniMenu()
registracija()


