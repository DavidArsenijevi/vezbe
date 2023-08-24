def proverasifre(sifra):
    if len(sifra) < 6:
        print("Šifra mora imati bar 6 karaktera")
        return False
    if not any(char.isdigit() for char in sifra):
        print("Šifra mora sadržavati bar 1 broj.")
        return False
    return True

def proveraPostojecegKorisnickogimena(korisnickoIme, nazivfajla):
    with open(nazivfajla, 'r') as fajl:
        sviKorisnici = fajl.readlines()
        postojecakorisnickaimena = [korisnik.split(' | ')[0] for korisnik in sviKorisnici]
        if korisnickoIme in postojecakorisnickaimena:
            return True
        return False

def registracijakorisnika(korisnickoIme, sifra, nazivfajla):
    with open(nazivfajla, 'a') as fajl:
        fajl.write(f"{korisnickoIme} | {sifra}\n")


def main():
    while True:
        korisnickoIme = input("Unesite korisničko ime: ")
        if korisnickoIme.strip() == "":
            print("Korisničko ime ne sme ostati prazno.")
            continue

        sifra = input("Unesite šifru: ")

        if not proverasifre(sifra):

            continue

        if proveraPostojecegKorisnickogimena(korisnickoIme, 'baza.txt'):
            print("Korisničko ime već postoji.")
            continue

        registracijakorisnika(korisnickoIme, sifra, 'baza.txt')
        print("Registracija uspešna.")

        registracija = input("Da li želite da se ponovo registrujete? (da/ne): ")
        if registracija.lower() != 'da':
            break

main()


