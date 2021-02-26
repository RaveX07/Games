import random

objekte = ["schere", "stein", "papier"]
urobj = input("Schere, Stein oder Papier?  ").lower()
objekt = random.choice(objekte)
print("\n" + objekt)

if urobj == "schere":
    if objekt == "schere":
        print("Unentschiden!\n")
    elif objekt == "stein":
        print("Du hast verloren!\n")
    elif objekt == "papier":
        print("Du hast gewonnen!\n")
elif urobj == "stein":
    if objekt == "stein":
        print("Unentschiden!\n")
    elif objekt == "papier":
        print("Du hast verloren!\n")
    elif objekt == "schere":
        print("Du hast gewonnen!\n")
elif urobj == "papier":
    if objekt == "papier":
        print("Unentschiden!\n")
    elif objekt == "schere":
        print("Du hast verloren!\n")
    elif objekt == "stein":
        print("Du hast gewonnen!\n")
else:
    print("Keine gültige Eingabe!\n")
