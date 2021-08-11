#!/usr/bin/env python

import random

def show_banner():
    print("")
    print(" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
    print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print("| |  ____  ____  | || |     _____    | || |    ______    | || |  ____  ____  | || |  _________   | || |  _______     | |")
    print("| | |_   ||   _| | || |    |_   _|   | || |  .' ___  |   | || | |_   ||   _| | || | |_   ___  |  | || | |_   __ \\    | |")
    print("| |   | |__| |   | || |      | |     | || | / .'   \\_|   | || |   | |__| |   | || |   | |_  \\_|  | || |   | |__) |   | |")
    print("| |   |  __  |   | || |      | |     | || | | |    ____  | || |   |  __  |   | || |   |  _|  _   | || |   |  __ /    | |")
    print("| |  _| |  | |_  | || |     _| |_    | || | \\ `.___]  _| | || |  _| |  | |_  | || |  _| |___/ |  | || |  _| |  \\ \\_  | |")
    print("| | |____||____| | || |    |_____|   | || |  `._____.'   | || | |____||____| | || | |_________|  | || | |____| |___| | |")
    print("| |              | || |              | || |              | || |              | || |              | || |              | |")
    print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
    print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")
    print("")
    print("         .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
    print("        | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print("        | |   _____      | || |     ____     | || | _____  _____ | || |  _________   | || |  _______     | |")
    print("        | |  |_   _|     | || |   .'    `.   | || ||_   _||_   _|| || | |_   ___  |  | || | |_   __ \\    | |")
    print("        | |    | |       | || |  /  .--.  \\  | || |  | | /\\ | |  | || |   | |_  \\_|  | || |   | |__) |   | |")
    print("        | |    | |   _   | || |  | |    | |  | || |  | |/  \\| |  | || |   |  _|  _   | || |   |  __ /    | |")
    print("        | |   _| |__/ |  | || |  \\  `--'  /  | || |  |   /\\   |  | || |  _| |___/ |  | || |  _| |  \\ \\_  | |")
    print("        | |  |________|  | || |   `.____.'   | || |  |__/  \\__|  | || | |_________|  | || | |____| |___| | |")
    print("        | |              | || |              | || |              | || |              | || |              | |")
    print("        | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
    print("         '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")
    print("")

def choose_number():
    number = random.randint(1, 100)

    return number

def guess_number():
    while True:
        guess = input("Pick a number between 1-100: ")

        # What to do if the user gives us something that isn't a number?
        try:
            guess = int(guess)
        except:
            print("Your guess has to be a number!")
            print("")
            continue

        # What to do if the user picks an invalid number?
        if guess < 1 or guess > 100:
            print("Your guess has to be between 1-100!")
            print("")
            continue

        break

    # At this point guess should contain a valid number between 1-100
    return guess

def show_count(count):
    if count == 1:
        print("That was your first guess!")
    else:
        print(f"You're at {count} guesses")
    print("")

def main():
    # Welcome the user to the game
    show_banner()

    # Initialize the game state (User picks the highest number)
    number = choose_number()
    guess_count = 0

    # Keep running the game until there's a win condition
    while True:
        # Have the user pick a number
        guess = guess_number()
        guess_count += 1

        if guess < number:
            print("Higher!")
            show_count(guess_count)

        elif guess > number:
            print("Lower!")
            show_count(guess_count)

        else:
            print("Winner winner chicken dinner!")
            print(f"It took you {guess_count} tries!")

            print("")
            print("Let's play again soon!!!")
            print("")

            # Breaks out of the game loop
            break

if __name__ == '__main__':
    random.seed()
    main()
