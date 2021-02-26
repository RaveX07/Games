import random
import words
import time

def stage(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
playing = True
while playing:
    completion = []
    word = random.choice(words.words).upper()
    word_completion = "-" * len(word)
    guessedletters = []
    guessed = False
    tries = 6            
    print("Lass uns Hangman spielen! ")
    while guessed == False and tries > 0:
        print(word_completion)
        letter = input("Tippe einen Buchstabe ein: ").upper()
        if letter in word and letter not in guessedletters:
            print("Richtig. Dieser Buchstabe ist in dem Wort enthalten.")
            print(stage(tries))
            guessedletters.append(letter)
            index = word.find(letter)
            word_as_list = list(word_completion)
            indices = [i for i, guess in enumerate(word) if guess == letter]
            for index in indices:
                word_as_list[index] = letter
            word_completion = "".join(word_as_list)
            if "-" not in word_completion:
                guessed = True
        elif letter not in word and letter not in guessedletters:
            print("Leider falsch. Dieser Buchstabe ist nicht im Wort enthalten. ")
            tries -= 1
            print(stage(tries))
            guessedletters.append(letter)
        elif letter in guessedletters:
            print("Diesen Buchstabe hast du schon einmal eingegeben. ")
        if guessed and tries > 0:
            print("Du hast gewonnen. Das Wort war " + word)
            playing = False
        elif not guessed and tries <= 0:
            print(stage(tries))
            print("Du hast leider keine Versuche mehr übrig. Du hast verloren. ")
            playing = False
            print(f"Das Wort war {word}. ")
    ok = input("Willst du nochmal spielen? [ja/nein]  ")
    if ok == "ja":
        playing = True
time.sleep(1)
    