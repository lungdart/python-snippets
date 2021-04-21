### IMPORTS
import sys
import random


### GLOBAL VALUES
WORDS = [
    "Adore", "Honey", "Affection", "Hugs", "Amour", "Appreciation", "Arrow",
    "Jewelry", "Baby", "Juliet", "Balloons", "Kisses", "Lace", "Beauty", "Locket",
    "Beloved", "Love", "Bliss", "Lovebirds", "Bow", "Lovers", "Candles", "Loving",
    "Candy", "Marriage", "Card", "Memories", "Champagne", "Moonstruck", "Cherish",
    "Chivalry", "Party", "Chocolates", "Pink", "Poem", "Couples", "Promise",
    "Courtship", "Proposal", "Crush", "Cuddle", "Red", "Cupid", "Ribbon", "Dance",
    "Ring", "Darling", "Romance", "Dates", "Romeo", "Dear", "Roses", "Dearest",
    "Desire", "Serenade", "Devotion", "Diamond", "Smooch", "Dinner", "Snuggle",
    "Embrace", "February", "Feelings", "Stunning", "Flirt", "Sweethearts",
    "Flowers", "Sweetie", "Forever", "Friends", "Together", "Friendship", "Treats",
    "Gentleman", "Gift", "Trust", "Unity", "Handsome", "Valentine", "Hearts",
    "Wedding", "Holiday"
]


### Game functions
def display_banner():
    print(r'''

,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,
88888888888     88888888888     88888888888     88888888888     88888888888
`Y8888888Y'     `Y8888888Y'     `Y8888888Y'     `Y8888888Y'     `Y8888888Y'
  `Y888Y'         `Y888Y'         `Y888Y'         `Y888Y'         `Y888Y'
    `Y'             `Y'             `Y'             `Y'             `Y'

                        Valentine's Word Scramble!
    ''')

def display_goodbye():
    print(r'''
           @@@   @@@       @@@   @@@       @@@   @@@       @@@   @@@
          @   @ @   @     @   @ @   @     @   @ @   @     @   @ @   @
\\\\      @    @    @     @    @    @     @    @    @     @    @    @
    ------@  )---(  @-----@  )---(  @-----@  )---(  @-----@  )---(  @------->
////       @       @       @       @       @       @       @       @
            @     @         @     @         @     @         @     @
             @   @           @   @           @   @           @   @
              @ @             @ @             @ @             @ @
               @               @               @               @)

                              Thanks for Playing!
                                  See you soon
    ''')

def scramble_word(word):
    # Convert the word to a list of characters so it can be used in the shuffler
    character_list = list(word)
    random.shuffle(character_list)

    # Return the shuffled list of characters to a single string
    scrambled_word = ''.join(character_list).lower()
    return scrambled_word

def game_loop():
    """ The main loop of the game containing all the logic """

    # To prevent the program from closing after a single game, we loop until
    #  the player no longer want's to play.
    score = 0
    while True:
        print("")
        print("Searching for the next word...")
        print("")

        random_word = random.choice(WORDS)
        scrambled_word = scramble_word(random_word)

        print("Guess the following word:")
        prompt = "{}: ".format(scrambled_word)
        guess = input(prompt)

        # Only increment the score on correct guesses
        if guess.lower() == random_word.lower():
            print("That's correct!")
            score += 1
        else:
            print("That's not quite it...")

        # Let the user decide if the game continues
        print("")
        print("Score: {}".format(score))
        try_again = input("Try again? [Y/n]")

        # Branch off what the user decides
        if try_again.lower() in ["n", "no"]:
            break
        elif try_again.lower() in ["y", "yes"]:
            continue
        else:
            # Oh no! Invalid input! Panic!!!
            raise Exception("Invalid Choice")

    print("")
    print("See you next time!")
    print("")


### MAIN()
def main():
    """ Main entry point for the program """

    # Because computers are never actually random. We need to "seed" the
    #  random number generator with something that is hard to predict. By
    #  default, this function "seeds" with the current time, which is a common
    #  practice.
    random.seed()

    # Game steps
    try:
        display_banner()
        game_loop()
        display_goodbye()
    except:
        # SOMETHING WEN"T WRONG! OH NO!
        return 42

    # We're done, return 0 to indicate everything worked correctly
    return 0

if __name__ == '__main__':
    # Return codes are ways to identify if a program succeeded at it's task.
    #  By convention, a 0 is a success, and any other number is a failure.
    #  programmers use these numbers and error code lookup tables to see what
    #  went wrong in programs while debugging.
    return_code = main()
    sys.exit(return_code)
