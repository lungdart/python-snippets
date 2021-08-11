#!/usr/bin/env python
import random

### GLOBAL VARIABLES
BANNER = """
 ___  ____  __  __  _____  _  _    ___    __   _  _  ___
/ __)(_  _)(  \\/  )(  _  )( \\( )  / __)  /__\\ ( \\/ )/ __)
\\__ \\ _)(_  )    (  )(_)(  )  (   \\__ \\ /(__)\\ \\  / \\__ \\
(___/(____)(_/\\/\\_)(_____)(_)\\_)  (___/(__)(__)(__) (___/
"""

ACTIONS = [
    "run",
    "jump",
    "scream",
    "fall",
    "wave",
    "dance",
    "freeze",
    "laugh",
    "moo",
    "meow",
    "bark",
    "salute",
    "sneeze",
    "sit",
    "swim",
    "yawn"
]

### FUNCTIONS
def print_hello(message):
    """ Introduces the player to the game """
    print(message)
    print("")

def get_random_action(actions):
    """ Chooses a random action from the given list """
    choice = random.choice(actions)
    return choice

def random_simon_says(percentage):
    """ Chooses if simon says or not """
    random_value = random.uniform(0.0, 1.0)
    if random_value < percentage:
        return True
    else:
        return False

def demand_action(simon_says, action):
    """ Demands the player to perform the action """
    print("") # Add a blank line before the simon says for styling

    if simon_says:
        what_the_user_did = input(f"Simon says to {action}:\n").lower()
        if what_the_user_did == action:
            return True
        else:
            return False

    else:
        what_the_user_did = input(f"Now {action}!\n").lower()
        if what_the_user_did == "":
            return True
        else:
            return False

def print_goodbye():
    """ Gracefully let the player down """
    print("-------------------")
    print("Neener neener, you lose!")
    print("   - Beter luck next time!!!")


### MAIN
def main():
    """ This is where the program starts from """
    print_hello(BANNER)

    while True:
        # Simon says ...
        action = get_random_action(ACTIONS)
        simon_says = random_simon_says(0.75)

        # Stop playing if the player ever fails!
        successful = demand_action(simon_says, action)
        if not successful:
            break

    # At this point, we're broken out of the loop because the player lost
    print_goodbye()

if __name__ == '__main__':
    main()
