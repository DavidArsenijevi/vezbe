broj = int(input("unesi broj:"))

if broj%2 == 0:
    if broj>10:
        print("broj koji ste uneli je paran i veci je od 10")
    else:
        print("broj koji ste uneli je paran i nije veci od 10")

else:
    if broj>=5 and broj<=30:
        print("broj koji ste uneli nije paran i pripada opsegu od 5 do 30")
    else:
        print("broj koji ste uneli nije paran i ne pripada opsegu od 5 do 30")




