spisak = ["svetionici", "pivara", "svilara"]
while True:
    unos = input("unesite nepokretno kulturno dobro:")
    if unos not in spisak:
        spisak.append(unos)
    print(spisak)
    pitanje = input("Da li zelite da unesete novo NKD? d-da n-ne").lower()
    while pitanje not in ["d", "n"]:
        pitanje = input("Uneli ste pogresno  slovo, pokusajte ponovo:").lower()
    if pitanje == "n":
        break

