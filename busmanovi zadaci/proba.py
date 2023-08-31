def provera_lozinke(lozinka):
    if len(lozinka) < 6:
        print("Šifra mora imati bar 6 karaktera")
        return False
    if not any(char.isdigit() for char in lozinka):
        print("Sifra mora imati barem 1 broj.")
        return False
    if not any(char.isupper() for char in lozinka) and any(char.islower() for char in lozinka):
        print("Sifra mora da ima jedno veliko i jedno malo slovo. ")
        return  False

    return True

def prijava():


    print("Dobrodosli! Unesite svoje korisničko ime i lozinku za prijavu.")
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



def registracija():

    print("Dobrodosli! Molimo unesite podatke za registraciju.")
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

        f = open("korisnici.txt","r")
        korisnici = f.readlines()
        for korisnik in korisnici:
            tokeni = korisnik.split("|")
            id = tokeni [0]
            uloga = tokeni [1]
            email_Adresa = tokeni [2]
            lozinka = tokeni [3]
            ime = tokeni [4]
            prezime = tokeni[5]
            adresa = tokeni [6]
            print(korisnik)


        break




def kupac(nazivfajla):
    registracija()
    while True:
            f = open(nazivfajla, "a")
            istorija_Porudzbine = input("Unesite porudzbinu: ")
            f.write(f"{istorija_Porudzbine}\n")















def main():
    print("Dobrodosli na nasu aplikaciju!")
    print("Izaberite opciju:")
    print("1 - Prijavite se")
    print("2 - Registrujte se")

    izbor = input("Unesite broj opcije: ")

    if izbor == "1":
        prijava()
    elif izbor == "2":
        registracija()
    else:
        print("Nevazeci unos. Molimo izaberite 1 ili 2.")
        main()



main()
kupac("porudzbine.txt")

