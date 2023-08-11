import random

x = 1
y = 0
upit = int(input("Koliko br zelite da unesete:"))
while x<=upit:
    broj = random.randint(1,100)
    print(broj)
    y = y+broj
    x+=1
print("srednja vrednost brojeva:",y/upit)



