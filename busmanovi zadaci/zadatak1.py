while True:
    korisnickoime = input("Unesite korisnicko ime:")
    sifra = input("Unesite sifru:")
    duzinaSifre = len(sifra)


    if duzinaSifre > 6:
        if any(chr.isdigit() for chr in sifra):
            file = open('baza.txt', 'r')
            content = file.read()

            if korisnickoime in content:
                print("To korisnicko ime je zauzeto, pokusajte neko drugo")

            else:
                f = open('baza.txt', 'a')
                f.write("Korisnicko ime: " + korisnickoime + ' | ' + ' sifra: ' + sifra + "\n")
                f.close()
                print("Registracija uspesna")

                registracija = input("da li zelite ponovo da se registrujete da/ne: ")
                if registracija == "ne":
                    break

                elif registracija == "da":
                    continue



                else:
                    print("Odgovor mora biti u formatu 'da' ili ne' ")
                    continue
        else:
            print("Sifra mora da sadrzi minimum 1 broj")
            continue




    else:
        print("Sifra mora da sadrzi 6 karaktera")
        continue








