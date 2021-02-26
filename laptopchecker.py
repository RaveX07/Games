
laptop = input("Welchen Laptop benutzt du?  ")
laptopnew = ""
for letter in laptop.lower():
    if letter != " ":
        laptopnew += letter
if "lenovothinkpad" in laptopnew:
    print("Gute Wahl!!! ")
else:
    print("Schlechte Entscheideung! ")
