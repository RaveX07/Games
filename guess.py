 
nameraw = input("\nGib hier deinen Namen ein: ")
name = nameraw.lower()
print("Das ist ein Ratespiel. Mal sehen ob du es schaffst.")
guess = input("\nWie alt ist R9?  ")
if guess == "44" and name == "karsten": 
    ja1 = input("Richtig! Wollen sie ein weiteres Rätsel machen? ja/nein: ")
    ja1_1 = ja1.lower()
    if ja1_1 == "ja":
        laptop = input("\nDarf sich Jannis einen neuen Laptop kaufen? ja/nein: ")
        if laptop == "nein":
            print("\nFalsche Antwort. Hier die Begründung:")
            print("\n1. Leo hat auch einen neuen Computer bekommen.\n2. Der alte Laptop von Jannis ist sehr sehr sehr langsam und hat einen kleinen Akku.")
            print("3. Den alten Laptop von Jannis können dann die anderen Familienmitglieder benutzen, z.B. zum shoppen.")
            print("4. Jannis darf sich auch mal was gönnen!\n")
            print("Hoffentlich sind sie jetzt davon überzeugt, dass Jannis einen neuen Laptop bekommen soll.")
            print("Falls nicht wenden sie sich bitte an den Coder dieses Programmes, in dem Fall ist das Jannis.\n")
        elif laptop == "ja":
            print("Diese Antwort ist richtig! Dann kann ich mir die Beründung ja ersparen.\n")
            beg = input("Willst du die Begründung doch hören ? ja/nein: ")
            beg1 = beg.lower()
            if beg1 == "ja":
                print("\n1. Leo hat auch einen neuen Computer bekommen.\n2. Der alte Laptop von Jannis ist sehr sehr sehr langsam und hat einen kleinen Akku.")
                print("3. Den alten Laptop von Jannis können dann die anderen Familienmitglieder benutzen, z.B. zum shoppen.")
                print("4. Jannis darf sich auch mal was gönnen!\n")
            else:
                print("Ok, dann halt nicht. ")
elif guess != "44" and name == "karsten": 
    ja2 = input("Leider falsch! Möchten sie mit einem anderen Rätsel fortfahren? ja/nein: ")
    ja2_1 = ja2.lower()
    if ja2_1 == "ja":
        laptop = input("\nDarf sich Jannis einen neuen Computer kaufen? ja/nein: ")
        if laptop == "nein":
            print("\nDas war leider die falsche Antwort, hier ist warum:")
            print("\n1. Leo hat auch einen neuen Computer bekommen.\n2. Der alte Laptop von Jannis ist sehr sehr sehr langsam und hat einen kleinen Akku.")
            print("3. Den alten Laptop von Jannis können dann die anderen Familienmitglieder benutzen, z.B. zum shoppen.")
            print("4. Jannis darf sich auch mal was gönnen!\n")
            print("Hoffentlich sind sie jetzt davon überzeugt, dass Jannis einen neuen Laptop bekommen soll.")
            print("Falls nicht wenden sie sich bitte an den Coder dieses Programmes, in dem Fall ist das Jannis.\n")
        elif laptop == "ja":
            print("Richtige Antwort! Dann kann ich mir die Begrüngung ja ersparen.\n")
            beg = input("Willst du die Begründung doch hören ? ja/nein: ")
            beg1 = beg.lower()
            if beg1 == "ja":
                print("\n1. Leo hat auch einen neuen Computer bekommen.\n2. Der alte Laptop von Jannis ist sehr sehr sehr langsam und hat einen kleinen Akku.")
                print("3. Den alten Laptop von Jannis können dann die anderen Familienmitglieder benutzen, z.B. zum shoppen.")
                print("4. Jannis darf sich auch mal was gönnen!\n")
            else:
                print("Ok, dann halt nicht. ")
elif guess != "44" and name != "karsten":
    print("Leider ist die Antwort falsch! \n")
elif guess == "44" and name != "karsten":
    print("Die Antwort war richtig. Du hast gewonnen! \n")    
 