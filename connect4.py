""" TIC TAC TOE """

def draw_board(board):
    """ Draw the board state to the window """
    print("1 2 3 4 5 6 7")
    print("-------------")
    print(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6])
    print(board[1][0], board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6])
    print(board[2][0], board[2][1], board[2][2], board[2][3], board[2][4], board[2][5], board[2][6])
    print(board[3][0], board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6])
    print(board[4][0], board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6])
    print(board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6])

def check_full(board):
    """ Check if the board is full """
    # The board is not full if any cell is empty. We can optimize this check by
    # starting at the last row first and work our way up.
    for row in board[:-1]:
        for cell in row:
            if cell == ' ':
                return False

    # Board must be full
    return True

def check_win(board):
    """ Check for a win condition returning the player value of who won """
    # Generate a list of wining positions on the board.
    # Rows
    for row in range(6):
        # There are 4 winning positions in each row:
        #   X X X X _ _ _
        #   _ X X X X _ _
        #   _ _ X X X X _
        #   _ _ _ X X X X
        for start in range(4):
            if (board[row][start] != ' ') and (
                    (board[row][start] == board[row][start+1]) and
                    (board[row][start] == board[row][start+2]) and
                    (board[row][start] == board[row][start+3])
            ):
                return board[row][start]

    # Check Columns
    for col in range(7):
        # There are 3 winning positions in each column:
        #   X _ _
        #   X X _
        #   X X X
        #   X X X
        #   _ X X
        #   _ _ X
        for start in range(3):
            if (board[start][col] != ' ') and (
                    (board[start][col] == board[start+1][col]) and
                    (board[start][col] == board[start+2][col]) and
                    (board[start][col] == board[start+3][col])
            ):
                return board[start][col]

    # Check Diagonals. There are 24 ways to make a diagonal. These are a too
    #  numerous to show in the comment.
    diagonal_wins = (
        ((3, 0), (2, 1), (1, 2), (0, 3)),
        ((4, 0), (3, 1), (2, 2), (1, 3)),
        ((5, 0), (4, 1), (3, 2), (2, 3)),

        ((3, 1), (2, 2), (1, 3), (0, 4)),
        ((4, 1), (3, 2), (2, 3), (1, 4)),
        ((5, 1), (4, 2), (3, 3), (2, 4)),

        ((3, 2), (2, 3), (1, 4), (0, 5)),
        ((4, 2), (3, 3), (2, 4), (1, 5)),
        ((5, 2), (4, 3), (3, 4), (2, 5)),

        ((3, 3), (2, 4), (1, 5), (0, 6)),
        ((4, 3), (3, 4), (2, 5), (1, 6)),
        ((5, 3), (4, 4), (3, 5), (2, 6)),


        ((3, 6), (2, 5), (1, 4), (0, 3)),
        ((4, 6), (3, 5), (2, 4), (1, 3)),
        ((5, 6), (4, 5), (3, 4), (2, 3)),

        ((3, 5), (2, 4), (1, 3), (0, 2)),
        ((4, 5), (3, 4), (2, 3), (1, 2)),
        ((5, 5), (4, 4), (3, 3), (2, 2)),

        ((3, 4), (2, 3), (1, 2), (0, 1)),
        ((4, 4), (3, 3), (2, 2), (1, 1)),
        ((5, 4), (4, 3), (3, 2), (2, 1)),

        ((3, 3), (2, 2), (1, 1), (0, 0)),
        ((4, 3), (3, 2), (2, 1), (1, 0)),
        ((5, 3), (4, 2), (3, 1), (2, 0)),
    )
    for line in diagonal_wins:
        pos1 = board[line[0][0]][line[0][1]]
        pos2 = board[line[1][0]][line[1][1]]
        pos3 = board[line[2][0]][line[2][1]]
        pos4 = board[line[3][0]][line[3][1]]
        if pos1 != ' ' and (
                pos1 == pos2 and
                pos1 == pos3 and
                pos1 == pos4
        ):
            return pos1

    # No win condition
    return False

def player_move(board, player):
    """ Get a player to make a move """
    # Continue to check for a valid move
    while True:
        print("Make a move {}: ".format(player))
        move = input()

        # Check for nonsensical move inputs
        valid_columns = ('1', '2', '3', '4', '5', '6', '7')
        if move not in valid_columns:
            print("Invalid input! try again...")
            continue

        # Check that the column is not full
        col_idx = int(move) - 1
        if board[0][col_idx] != ' ':
            print("There are no empty spaces left in that column! Try again...")
            continue

        # VALID MOVE
        # Discover the bottom most empty row in that column to put the players
        #  token in
        bottom_idx = 0
        for row_idx in (1, 2, 3, 4, 5):
            if board[row_idx][col_idx] == ' ':
                bottom_idx = row_idx

        # Update the board state with the players token
        board[bottom_idx][col_idx] = player
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
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

    # Game loop
    player = 'R'
    while not check_full(board):
        # Draw the board and get the players move
        draw_board(board)
        player_move(board, player)

        # Check if the game is over
        if check_win(board):
            draw_board(board)
            game_over(won=True, player=player)
            return

        # Prepare the next player
        if player == 'R':
            player = 'Y'
        else:
            player = 'R'

    # Board is full and no win condition detected. Tie game.
    draw_board(board)
    game_over(won=False)
    return

# Configure main() as the entry point
if __name__ == '__main__':
    main()
