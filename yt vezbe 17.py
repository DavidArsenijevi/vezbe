podaci = input("Unesite duzinu i sirinu pravougaonika:")
stranice = podaci.split(" ")
print(stranice)

obim = 2*float(stranice[0])+2*float(stranice[1])
povrsina = float(stranice[0])*float(stranice[1])

print("0 =",obim)
print("p =", povrsina)
