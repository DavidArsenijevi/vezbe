opstina = ["Smederevo"]
opstina.append("Vrsac")
opstina.append("Velika Plana")
opstina.append("Smederevska Palanka")
opstina.append("Kovin")
opstina.append("Pancevo")
opstina.append("Pozarevac")
opstina.append("Bela Crkva")
print(opstina)
print("Duzina liste:",len(opstina))
opstina.remove("Vrsac")
opstina.sort()
print(opstina)
opstina.sort(reverse=True)
print(opstina)
print(opstina.index("Pancevo"))