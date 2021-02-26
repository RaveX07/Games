import random
import string

scores = open("stadtscore.txt", "r+")
scoresr = scores.readlines()
scorelist = []
failed = False
for line in scoresr:
    if line[-1] == "\n":
        scorelist.append(int(line[:-1]))
    else:
        scorelist.append(int(line))
scorelist.sort()
try:
    highscore = scorelist[-1]
except:
    highscore = 0
score = 0

ok = input("Willst du ein Ratespiel spielen? ")
if ok == "ja":
    print(f"Dein bisheriger Highscore ist {highscore}. ")
    munich = 1400000
    hamburg = 1800000
    berlin = 3700000
    koln = 1100000
    frankfurt = 750000
    stuttgart = 650000
    leipzig = 600000
    dortmund = 580000

    munichn = "München"
    hamburgn = "Hamburg"
    berlinn = "Berlin"
    kolnn = "Köln"
    frankfurtn = "Frankfurt"
    stuttgartn = "Stuttgart"  
    leipzign = "Leipzig"
    dortmundn = "Dortmund"
    städte = [munichn, hamburgn, stuttgartn, kolnn, berlinn, frankfurtn, leipzign, dortmundn]

    while not failed:
        stadt1 = random.choice(städte)
        if stadt1 == munichn:
            istadt1 = munich
        elif stadt1 == hamburgn:
            istadt1 = hamburg
        elif stadt1 == stuttgartn:
            istadt1 = stuttgart 
        elif stadt1 == kolnn:
            istadt1 = koln 
        elif stadt1 == berlinn:
            istadt1 = berlin
        elif stadt1 == dortmundn:
            istadt1 = dortmund 
        elif stadt1 == leipzign:
            istadt1 = leipzig 
        elif stadt1 == frankfurtn:
            istadt1 = frankfurt

        stadt2 = random.choice(städte)
        while stadt1 == stadt2:
            stadt2 = random.choice(städte)

        if stadt2 == munichn:
            istadt2 = munich
        elif stadt2 == hamburgn:
            istadt2 = hamburg
        elif stadt2 == stuttgartn:
            istadt2 = stuttgart 
        elif stadt2 == kolnn:
            istadt2 = koln 
        elif stadt2 == berlinn:
            istadt2 = berlin
        elif stadt2 == dortmundn:
            istadt2 = dortmund 
        elif stadt2 == leipzign:
            istadt2 = leipzig 
        elif stadt2 == frankfurtn:
            istadt2 = frankfurt

        while stadt1 == stadt2:
            stadt1 = random.choice(städte)
        guess = input(f"Welche Stadt ist größer: {stadt1} oder {stadt2}? ")
        if istadt1 < istadt2:
            if guess == stadt2:
                score += 1
                print("Gut das war richtig! ")
                print(f"Dein Score ist {int(score)}")
            else:
                failed = True
                print("Das war leider falsch! ")
        if istadt1 > istadt2:
            if guess == stadt1:
                score += 1
                print("Gut das war richtig! ")
                print(f"Dein Score ist {int(score)}")
            else:
                print("Das war leider falsch!")
                failed = True
        

scores.write(f"\n{str(score)}")
scores.close()
