""" TIC TAC TOE """

from os import system, name

def clear():
    """ Clears the screen """
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def draw_board(board):
    """ Draw the board state to the window """
    print("    1 2 3")
    print("--+------")
    print("A | {0} {1} {2}".format(board[0][0], board[0][1], board[0][2]))
    print("B | {0} {1} {2}".format(board[1][0], board[1][1], board[1][2]))
    print("C | {0} {1} {2}".format(board[2][0], board[2][1], board[2][2]))

def check_full(board):
    """ Check if the board is full """
    # The board is not full if any cell is empty
    for row in board:
        for cell in row:
            if cell == ' ':
                return False

    # Board must be full
    return True

def check_win(board):
    """ Check for a win condition returning the player value of who won """
    # Check rows
    for row in range(3):
        if (board[row][0] != ' ') and (board[row][0] == board[row][1]) and (board[row][0] == board[row][2]):
            return board[row][0]

    # Check Columns
    for col in range(3):
        if (board[0][col] != ' ') and (board[0][col] == board[1][col]) and (board[0][col] == board[2][col]):
            return board[0][col]

    # Check Diagonals
    if (board[0][0] != ' ') and (board[0][0] == board[1][1]) and (board[0][0] == board[2][2]):
        return board[0][0]
    if (board[0][2] != ' ') and (board[0][2] == board[1][1]) and (board[0][2] == board[2][0]):
        return board[0][2]

    # No win condition
    return False

def player_move(board, player):
    """ Get a player to make a move """
    # Take note of valid moves
    rows = ('A', 'B', 'C')
    cols = ('1', '2', '3')

    # Continue to check for a valid move
    while True:
        print("Make a move {}: ".format(player))
        move = input()

        # Check for nonsensical moves
        if move[0].upper() not in rows or move[1] not in cols:
            print("Invalid input! try again...")
            continue

        # Check for duplicate moves
        row = rows.index(move[0].upper())
        col = cols.index(move[1])
        cell = board[row][col]
        if cell != ' ':
            print("That spot is already taken! Try again...")
            continue

        # Valid move given, update the board state
        board[row][col] = player
        return

def game_over(won=False, player=None):
    """ Announces the game is over """
    if won:
        print("A winner is {}".format(player))
    else:
        print("Tie game! See you next time...")

def main():
    """ Entry point for program """
    # Configure state
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    # Game loop
    player = 'X'
    while not check_full(board):
        # Draw the board and get the players move
        clear()
        draw_board(board)
        player_move(board, player)

        # Check if the game is over
        if check_win(board):
            draw_board(board)
            game_over(won=True, player=player)
            return

        # Prepare the next player
        if player == 'X':
            player = 'Y'
        else:
            player = 'X'

    # Board is full and no win condition detected. Tie game.
    draw_board(board)
    game_over(won=False)
    return

# Configure main() as the entry point
if __name__ == '__main__':
    main()
