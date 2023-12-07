import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = input("Neue Zahl: ")
    if guess > 0:
        if guess > to_be_guessed:
            print("Zahl zu groß")
        elif guess < to_be_guessed:
            print("Zahl zu klein")
    else:
        print("Schade, Sie geben also auf!")
        break
else:
    print("Glückwunsch! Das war's!")