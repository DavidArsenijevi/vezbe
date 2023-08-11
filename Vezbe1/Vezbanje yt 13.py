frekvencija = float(input("unesite frekvenciju u MHz:"))
if frekvencija >=3 and frekvencija<30:
    print("dekametarski - kratki talasi")
    print("HF")

elif frekvencija>=30 and frekvencija<300:
    print("metarski - ultra kratki talasi")
    print("VHF")

elif frekvencija>=300 and frekvencija<3000:
    print("decimetarski talasi")
    print("UHF")

elif frekvencija>=3000 and frekvencija<=30000:
    print("centimetarski talasi")
    print("SHF")

else:
    print("uneta frekvencija ne pripada nijednom opsegu")
