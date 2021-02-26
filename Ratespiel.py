
secret = "1899"
guesses = 0
guesslimit = 5
left = guesslimit - guesses
strleft = str(left)
limit = False
tips = ["Barca wurde vor 1900 gegründet.", "Barca wurde nach 1800 gegründet.", "Barca wurde nach 1850 gegründet.", "Die letzte Ziffer ist eine 9.",]

print("\nDas ist ein Ratespiel. Mal sehen ob du es schaffst.")
guess = input("In welchem Jahr wurde der FC Barcelona gegründet? Du hast 5 Versuche.  ")

while guess != secret and not(limit):
    x = guesses
    guesses += 1
    left = guesslimit - guesses
    strleft = str(left)
    if guesses >= 4:
        limit = True
    print("\nDas war leider die falsche Antwort.\n")
    for x in range(guesses):
        print(tips[x])
    guess = input("\nVersuche es nochmal. Du hast noch " + strleft + " Versuch(e) übrig.\nIn welchem Jahr wurde der FC Barcelona gegründet?  ")
if limit: 
    print("\nDu hast keine Versuche übrig. Du hast leider verloren.")
elif guess == "1899" and not(limit):
    print("\nRichtig! Du hast gewonnen!")
        

