import random
import time

winners = open("winner.txt", "r+")

namelist = []
letters = ["X", "O"]
namep1 = input("Spiler 1 was ist dein Name?  ").upper()
namep2 = input("Spieler 2 was ist dein Name? ").upper()
namelist.append(namep1)
namelist.append(namep2)
lp1 = random.choice(letters)
lp2 = random.choice(letters)
while lp1 == lp2:
    lp2 = random.choice(letters)
p1 = random.choice(namelist)
p2 = random.choice(namelist)
while p2 == p1:
    p2 = random.choice(namelist)
namelist.append(namep1)
namelist.append(namep2)
winnerlist = []

for line in winners:
    if line[-1] == "\n":
        winnerlist.append(line[:-1])
    else:
        winnerlist.append(line)

winsp1 = winnerlist.count(namep1)
winsp2 = winnerlist.count(namep2)

print(f"{namep1} hat bis jetzt {winsp1} mal gewonnen und {namep2} hat bis jetzt {winsp2} mal gewonnen.")

freespaces = []
board = [" " for x in range(9)]

win = False
full = False


def is_winner(letter):
    if (board[0] == letter and board[1] == letter and board[2] == letter) or (
            board[3] == letter and board[4] == letter and board[5] == letter) or (
            board[6] == letter and board[7] == letter and board[8] == letter) or (
            board[0] == letter and board[4] == letter and board[8] == letter) or (
            board[0] == letter and board[3] == letter and board[6] == letter) or (
            board[1] == letter and board[4] == letter and board[7] == letter) or (
            board[2] == letter and board[4] == letter and board[6] == letter) or (
            board[2] == letter and board[5] == letter and board[8] == letter):
        win = True
        return (win)


def who_winner():
    if (board[0] == lp1 and board[1] == lp1 and board[2] == lp1) or (
            board[3] == lp1 and board[4] == lp1 and board[5] == lp1) or (
            board[6] == lp1 and board[7] == lp1 and board[8] == lp1) or (
            board[0] == lp1 and board[4] == lp1 and board[8] == lp1) or (
            board[0] == lp1 and board[3] == lp1 and board[6] == lp1) or (
            board[1] == lp1 and board[4] == lp1 and board[7] == lp1) or (
            board[2] == lp1 and board[4] == lp1 and board[6] == lp1):
        winner = p1
    elif (board[0] == lp2 and board[1] == lp2 and board[2] == lp2) or (
            board[3] == lp2 and board[4] == lp2 and board[5] == lp2) or (
            board[6] == lp2 and board[7] == lp2 and board[8] == lp2) or (
            board[0] == lp2 and board[4] == lp2 and board[8] == lp2) or (
            board[0] == lp2 and board[3] == lp2 and board[6] == lp2) or (
            board[1] == lp2 and board[4] == lp2 and board[7] == lp2) or (
            board[2] == lp2 and board[4] == lp2 and board[6] == lp2):
        winner = p2
    return(winner)


def is_full():
    if (board[0] in letters and board[1] in letters and board[2] in letters and board[3] in letters and board[
        4] in letters and board[5] in letters and board[6] in letters and board[7] in letters and board[8] in letters):
        full = True
        return (full)


def spaces_free():
    freespaces.clear()
    for i in range(9):
        if board[i] == " ":
            freespaces.append(i)


def move(player, lp):
    print(f"Spieler {player} du bist an der Reihe.")
    try:
        posletter = int(input(f"Wo soll das {lp} hin? ")) - 1
    except:
        print("Das ist keine gültige Position.")
        posletter = int(input(f"Wo soll das {lp} hin? ")) - 1
    spaces_free()
    if posletter in freespaces:
        board[posletter] = lp
    while posletter not in freespaces:
        print("Keine gültige Position. ")
        posletter = int(input(f"Wo soll das {lp} hin? ")) - 1
        if posletter in freespaces:
            board[posletter] = lp
            break


def print_board():
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")


def main():
    print("Willkommen zu Tic Tac Toe! \n")
    print_board()
    win = is_winner(lp1)
    full = is_full()
    while not (full):
        move(p1, lp1)
        print_board()
        win = is_winner(lp1)
        full = is_full()
        if win or full:
            break
        move(p2, lp2)
        print_board()
        win = is_winner(lp2)
        full = is_full()
        if win or full:
            break

    if win:
        winner = who_winner()
        winners.write("\n" + winner.upper())
        print(f"Der Gewinner ist {winner}. ")
    if full and not win:
        print("Unentschieden. ")

ok = True
while ok:
    board.clear()
    board = [" " for x in range(9)]
    if p1 == namep1:
        p1 = namep2
        p2 = namep1
    else:
        p1 = namep1
        p2 = namep2
    if lp2 == "X":
        lp1 = "X"
        lp2 = "O"
    else:
        lp1 = "O"
        lp2 = "X"
    main()
    again = input("Willst du nochmal spielen? ")
    if again != "ja":
        ok = False
        break
time.sleep(1)
