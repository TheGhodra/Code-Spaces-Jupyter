import random

def schere_stein_papier():
    options = ["Schere", "Stein", "Papier"]

    print("Willkommen beim Schere, Stein, Papier Spiel!")

    while True:
        user_choice = input("Wähle Schere, Stein oder Papier (oder 'exit' zum Beenden): ").capitalize()

        if user_choice == 'Exit':
            print("Auf Wiedersehen!")
            break

        if user_choice not in options:
            print("Ungültige Eingabe. Bitte wähle Schere, Stein oder Papier.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer wählt: {computer_choice}")

        if user_choice == computer_choice:
            print("Unentschieden!")
        elif (
            (user_choice == "Schere" and computer_choice == "Papier") or
            (user_choice == "Stein" and computer_choice == "Schere") or
            (user_choice == "Papier" and computer_choice == "Stein")
        ):
            print("Du gewinnst!")
        else:
            print("Computer gewinnt!")

if __name__ == "__main__":
    schere_stein_papier()