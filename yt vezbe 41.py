x = ["b","c","a"]
print(x[0])

y = {"poz2":"b","poz3":"c","poz1":"a"}
print(y["poz1"])

z = ("a","b","c")
print(z[0])

#keys()
#values()
#items()
print(y.keys())
print(y.values())

for i in y.keys():
    print(i)
for i in y.values():
    print(i)
print(y.items())
for i,j in y.items():
    print(f"Kljuc: {i}, Vrednost: {j}")


print("-------------------")

recnik = {1:"a",2:{"ime":"David","prezime":"Arsenijevic"}}
print(recnik[2]["ime"])
recnik[3] = "c"
print(recnik)
recnik[2]["godine"]=21
print(recnik)
