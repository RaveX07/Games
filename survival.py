
print("Willkommen zu meinem ersten Spiel")
name = input("Was ist dein Name? ")
age = int(input("Hallo " + name + ", wie alt bist du? "))
health = 10
win = False

if age >= 12:
    ok = input("Ok. Du bist alt genug um dieses Spiel zu spielen.\nMöchtest du es spielen? (ja/nein)  ").lower()
    if ok == "ja":
        print("\nGut! Das ist ein Survival-Spiel. Du hast 10 Leben. Los gehts:")
        dec1 = input("\nDu weißt nicht wo du bist. Willst du rechts oder links gehen? (rechts/links)  ")
        if dec1 == "rechts" and health > 0:
            print("\nDu bist auf eine Schlucht zugelaufen und hineingefallen. Du hast verloren!")
        elif dec1 == "links" and health > 0:
            dec2 = input("\nDu kommst an einen See. Willst du durch ihn durch schwimmen oder um ihn herumlaufen? (schwimmen/laufen)  ").lower()
            if dec2 == "schwimmen" and health > 0:
                health -= 3
                print("\nDu hast es an das andere Ufer geschaft, aber wurdest von einer Qualle gebissen. Du verlierst 3 Leben und hast jetzt nur noch " + str(health) + ".")
                dec3 = input("Am anderen Ende des Ufers siehst du ein Haus und einen kleinen Fluss. Willst du zum Fluss gehen oder zum Haus gehen, um nach Hilfe zu fragen? (haus/fluss)  ").lower()
                if dec3 == "fluss" and health > 0:
                    print("\nDu bist in den Fluss gefallen und bist ertrunken. ")
                elif dec3 == "haus" and health > 0:
                    dec4 = input("\nDu gehst in das Haus. In dem Haus steht ein alter Mann.\nMöchtest du mit ihm reden oder lieber verschwinden? (bleiben/verschwinden)  ").lower()
                    if dec4 == "bleiben" and health > 0:
                        health -= 5
                        print("\nDer Mann im Haus geht mit einem Messer auf dich los. Er erwischt dich mit seinem Messer am Arm.\nDu kannst aber noch entwischen. Du hast nur noch " + str(health) + " Leben übrig")
                        dec5 = input("Du bist in einen Wald gerannt und weißt nicht wo du bist. Gehst du wieder zurück oder willst du weiter geradeaus laufen? (gerade/zurück)  ").lower()
                        if dec5 == "zurück" and health > 0:
                            health -= 8
                            print("\nDu läufst zurück. Am Ende des Waldes wartet der alte Mann mit seinem Messer. Er ist dir bis zum Wald gefolgt und greift dich mit seinem Messer an und sticht dir in den Bauch.\nDu hast jetzt noch " + str(health) + "Leben")
                            if health > 0:
                                dec6 = input("Du verläufst dich wieder im Wald und hast immer mehr Hunger. Als du raus läufst siehst du einen Struach Beeren und eine Wasserstelle.\nWillst du die Beeren essen und das Wasser trinken oder nach Hilfe suchen? (suchen/essen)  ")
                                if dec6 == "suchen" and health > 0:
                                    print("\nDu findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt")
                                elif dec6 == "essen" and health > 0:
                                    health -= 4
                                    print("\nDie Beeren waren giftig und das Wasser war auch verseucht. Du verlierst 4 Leben und hast nur noch " + str(health))
                                    if health > 0:
                                        print("Du gehst weiter und findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                        win = True
                            else:
                                print("Du hast nur noch " + str(health) + "Leben")
                        elif dec5 == "gerade" and health > 0:
                            print("\nDu läufst weiter und hast hunger. Irgendwann kommst du aus dem Wald wieder raus. Als du raus läufst siehst du einen Strauch Beeren und eine Wasserstelle.")
                            dec6 = input("Willst du von den Beeren essen und aus der Wasserstelle trinken oder willst du lieber weitergehen und nach Hilfe suchen? (suchen/essen)  ").lower()
                            if dec6 == "suchen" and health > 0:
                                print("\nDu findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                win = True
                            elif dec6 == "essen" and health > 0:
                                health -= 4
                                print("\nDie Beeren waren giftig und das Wasser war auch verseucht. Du verlierst 4 Leben und hast nur noch " + str(health))
                                if health > 0:
                                        print("Du gehst weiter und findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                        win = True
                    elif dec4 == "verschwinden" and health > 0:
                        print("\nDer Mann aus dem Haus rennt dir hinterher und du rennst weg.")
                        dec5 = input("Du bist in einen Wald gerannt und weißt nicht wo du bist. Gehst du wieder zurück oder willst du weiter geradeaus laufen? (gerade/zurück)  ").lower()
                        if dec5 == "zurück" and health > 0:
                            health -= 8
                            print("\nDu läufst zurück. Am Ende des Waldes wartet der alte Mann mit seinem Messer. Er ist dir bis zum Wald gefolgt und greift dich mit seinem Messer an und sticht dir in den Bauch.\nDu hast jetzt noch " + str(health) + "Leben")
                            if health > 0:
                                dec6 = input("Du verläufst dich wieder im Wald und hast immer mehr Hunger. Als du raus läufst siehst du einen Struach Beeren und eine Wasserstelle.\nWillst du die Beeren essen und das Wasser trinken oder nach Hilfe suchen? (suchen/essen)  ")
                                if dec6 == "suchen" and health > 0:
                                    print("\nDu findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt")
                                elif dec6 == "essen" and health > 0:
                                    health -= 4
                                    print("\nDie Beeren waren giftig und das Wasser war auch verseucht. Du verlierst 4 Leben und hast nur noch " + str(health))
                                    if health > 0:
                                        print("Du gehst weiter und findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                        win = True
                            else:
                                print("Du hast nur noch " + str(health) + "Leben")
                        elif dec5 == "gerade" and health > 0:
                            print("\nDu läufst weiter und hast hunger. Irgendwann kommst du aus dem Wald wieder raus. Als du raus läufst siehst du einen Strauch Beeren und eine Wasserstelle.")
                            dec6 = input("Willst du von den Beeren essen und aus der Wasserstelle trinken oder willst du lieber weitergehen und nach Hilfe suchen? (suchen/essen)  ").lower()
                            if dec6 == "suchen" and health > 0:
                                print("\nDu findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                win = True
                            elif dec6 == "essen" and health > 0:
                                health -= 4
                                print("\nDie Beeren waren giftig und das Wasser war auch verseucht. Du verlierst 4 Leben und hast nur noch " + str(health))
                                if health > 0:
                                        print("Du gehst weiter und findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                        win = True
            elif dec2 == "laufen" and health > 0:
                print("\nDu bist am anderen Ufer angekommen.")
                dec3 = input("Am anderen Ende des Ufers siehst du ein Haus und einen kleinen Fluss. Willst du zum Fluss oder zum Haus gehen, um nach Hilfe zu fargen? (haus/fluss)  ").lower()
                if dec3 == "fluss" and health > 0:
                    print("\nDu bist in den Fluss gefallen und bist ertrunken. ")
                elif dec3 == "haus" and health > 0:
                    dec4 = input("\nDu gehst in das Haus. In dem Haus steht ein alter Mann.\nMöchtest du mit ihm reden oder lieber verschwinden? (bleiben/verschwinden)  ").lower()
                    if dec4 == "bleiben" and health > 0:
                        health -= 5
                        print("\nDer Mann im Haus geht mit einem Messer auf dich los. Er erwischt dich mit seinem Messer am Arm.\nDu kannst aber noch entwischen. Du hast nur noch " + str(health) + " Leben übrig")
                        dec5 = input("Du bist in einen Wald gerannt und weißt nicht wo du bist. Gehst du wieder zurück oder willst du weiter geradeaus laufen? (gerade/zurück)  ").lower()
                        if dec5 == "zurück" and health > 0:
                            health -= 8
                            print("\nDu läufst zurück. Am Ende des Waldes wartet der alte Mann mit seinem Messer. Er ist dir bis zum Wald gefolgt und greift dich mit seinem Messer an und sticht dir in den Bauch.\nDu hast jetzt noch " + str(health) + "Leben")
                            if health > 0:
                                dec6 = input("Du verläufst dich wieder im Wald und hast immer mehr Hunger. Als du raus läufst siehst du einen Struach Beeren und eine Wasserstelle.\nWillst du die Beeren essen und das Wasser trinken oder nach Hilfe suchen? (suchen/essen)  ")
                                if dec6 == "suchen" and health > 0:
                                    print("\nDu findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt")
                                elif dec6 == "essen" and health > 0:
                                    health -= 4
                                    print("\nDie Beeren waren giftig und das Wasser war auch verseucht. Du verlierst 4 Leben und hast nur noch " + str(health))
                                    if health > 0:
                                        print("Du gehst weiter und findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                        win = True
                            else:
                                print("Du hast nur noch " + str(health) + "Leben")
                        elif dec5 == "gerade" and health > 0:
                            print("\nDu läufst weiter und hast hunger. Irgendwann kommst du aus dem Wald wieder raus. Als du raus läufst siehst du einen Strauch Beeren und eine Wasserstelle.")
                            dec6 = input("Willst du von den Beeren essen und aus der Wasserstelle trinken oder willst du lieber weitergehen und nach Hilfe suchen? (suchen/essen)  ").lower()
                            if dec6 == "suchen" and health > 0:
                                print("\nDu findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                win = True
                            elif dec6 == "essen" and health > 0:
                                health -= 4
                                print("\nDie Beeren waren giftig und das Wasser war auch verseucht. Du verlierst 4 Leben und hast nur noch " + str(health))
                                if health > 0:
                                        print("Du gehst weiter und findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                        win = True
                    elif dec4 == "verschwinden" and health > 0:
                        print("\nDer Mann aus dem Haus rennt dir hinterher und du rennst weg.")
                        dec5 = input("Du bist in einen Wald gerannt und weißt nicht wo du bist. Gehst du wieder zurück oder willst du weiter geradeaus laufen? (gerade/zurück)  ").lower()
                        if dec5 == "zurück" and health > 0:
                            health -= 8
                            print("\nDu läufst zurück. Am Ende des Waldes wartet der alte Mann mit seinem Messer. Er ist dir bis zum Wald gefolgt und greift dich mit seinem Messer an und sticht dir in den Bauch.\nDu hast jetzt noch " + str(health) + "Leben")
                            if health > 0:
                                dec6 = input("Du verläufst dich wieder im Wald und hast immer mehr Hunger. Als du raus läufst siehst du einen Struach Beeren und eine Wasserstelle.\nWillst du die Beeren essen und das Wasser trinken oder nach Hilfe suchen? (suchen/essen)  ")
                                if dec6 == "suchen" and health > 0:
                                    print("\nDu findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt")
                                elif dec6 == "essen" and health > 0:
                                    health -= 4
                                    print("\nDie Beeren waren giftig und das Wasser war auch verseucht. Du verlierst 4 Leben und hast nur noch " + str(health))
                                    if health > 0:
                                        print("Du gehst weiter und findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                        win = True
                            else:
                                print("Du hast nur noch " + str(health) + "Leben")
                        elif dec5 == "gerade" and health > 0:
                            print("\nDu läufst weiter und hast hunger. Irgendwann kommst du aus dem Wald wieder raus. Als du raus läufst siehst du einen Strauch Beeren und eine Wasserstelle.")
                            dec6 = input("Willst du von den Beeren essen und aus der Wasserstelle trinken oder willst du lieber weitergehen und nach Hilfe suchen? (suchen/essen)  ").lower()
                            if dec6 == "suchen" and health > 0:
                                print("\nDu findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                win = True
                            elif dec6 == "essen" and health > 0:
                                health -= 4
                                print("\nDie Beeren waren giftig und das Wasser war auch verseucht. Du verlierst 4 Leben und hast nur noch " + str(health))
                                if health > 0:
                                        print("Du gehst weiter und findest ein Haus. Du klingelst an der Tür und eine Hilfsbereite Dame macht dir auf, die dir etwas zu essen gibt und dich zurück nach Hause bringt.\n")
                                        win = True
if health < 0:
    print("\nDu hast keine Leben mehr. Du hast verloren!")
if health > 0 and win == True:
    print("\nDu hast gewonnen!!!")
elif age < 12:
    print("Du bist leider nicht alt genug für dieses Spiel.")
