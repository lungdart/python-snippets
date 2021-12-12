#!/usr/bin/env python
import random


### GLOBAL CONSTANT GAME DATA ###
REINDEER = ["dasher", "dancer", "prancer", "vixen", "comet", "cupid", "donner", "blitzen", "rudolph", "olive"]


### GAME FUNCTIONS ###
def show_welcome_screen():
    print(r'''
      _____________,--,
      | | | | | | |/ .-.\   GUESS SANTA'S
      |_|_|_|_|_|_/ /   `.     REINDEER
       |_|__|__|_; |      \
       |___|__|_/| |     .'`}
       |_|__|__/ | |   .'.'`\
       |__|__|/  ; ;  / /    \.-"-.
       ||__|_;   \ \  ||    /`___. \
       |_|___/\  /;.`,\\   {_'___.;{}
       |__|_/ `;`__|`-.;|  |C` e e`\
       |___`L  \__|__|__|  | `'-o-' }
       ||___|\__)___|__||__|\   ^  /`\
       |__|__|__|__|__|_{___}'.__.`\_.'}
       ||___|__|__|__|__;\_)-'`\   {_.-;
       |__|__|__|__|__|/` (`\__/     '-'
       |_|___|__|__/`      |
       |__|___|__/`         \-------------------
-.__.-.|___|___;`            |.__.-.__.-.__.-.__
  |     |     ||             |  |     |     |
-' '---' '---' \             /-' '---' '---' '--
     |     |    '.        .' |     |     |     |
'---' '---' '---' `-===-'`--' '---' '---' '---'
  |     |     |     |     |     |     |     |
-' '---' '---' '---' '---' '---' '---' '---' '--
     |     |     |     |     |     |     |     |
'---' '---' '---' '---' '---' '---' '---' '---'
''')


def get_random_reindeer():
    name = random.choice(REINDEER)
    return name

def play_a_round(name, max_guesses):
    current_guess = 0
    print("The computer is thinking of one of Santa's reindeer. Can you guess which one?")

    while current_guess < max_guesses:
        print(f"(You have {max_guesses - current_guess} guesses left to get it right!)")
        attempt = input("> ").lower()
        print("") # Add a blank new line for clarity

        # Let the player off easy if he can't remember the reindeer names
        if attempt not in REINDEER:
            print("That's not one of Santa's reindeer! I'll let you off easy this time. Try harder")
            continue

        # Let's mark the attempt after we know it's valid so the player actually
        #  get's a freebie like we said they would
        current_guess += 1

        # If the guess was correct, the round is over with a correct answer
        if attempt == name.lower():
            print(f"You win! It was {name.capitalize()}!!")
            return True

        # If the guess was wrong, but we have attempts left, loop around again
        if attempt != name.lower() and current_guess < max_guesses:
            print("Sorry! Try again...")
            continue

        # Finally the only option is that all guesses were exhausted and the player
        #  lost this round.
        print(f"Sorry, the correct reindeer was {name.capitalize()}. You lose this round...")
        return False



def ask_to_play_again():
    while True:
        # We ask the player if they like to play again
        play_again = input("Would you like to play again? [Y/n] ")

        # We need to convert the input into True or False. We need to handle the
        #  blank default case, yes, no, y and n.
        if play_again == '' or play_again.lower() == 'y' or play_again.lower() == "yes":
            return True

        if play_again.lower() == 'n' or play_again.lower() == 'no':
            return False

        # Any other choice is invalid, and we ask again
        print("Invalid choice. please use 'Yes' or 'No'")

def say_goodbye(score):
    print(f"Your final score was {score}! Hope to see you soon!")



### MAIN ENTRY POINT OF THE PROGRAM ###
def main():
    show_welcome_screen()
    score = 0

    playing = True
    while playing:
        # Pick a random reindeer and play a round
        name = get_random_reindeer()
        result = play_a_round(name, 3)

        # Increase score for correct guesses
        if result:
            score += 1

        # Continue?
        playing = ask_to_play_again()

    # Let the player down niceley while telling him his score!
    say_goodbye(score)
if __name__ == '__main__':
    main()
