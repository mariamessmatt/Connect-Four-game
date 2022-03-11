# _____________________________________________________________________________

#  This program represents "connect four" game using python
#  Written by : Mariam Esmat Ahmed

# _____________________________________________________________________________

# starting off with some constants declaring board dimensions
BOARD_COLUMNS = 7
BOARD_ROWS = 6

# then we will make a class that holds the board's information and state


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLUMNS)]
                      for _ in range(BOARD_ROWS)]  # A 2D array
        self.turns = 0   # staring with 0 turns
        self.final_move = [-1, -1]  # starting out of range of rows and columns

    def print_board(self):
        print("\n")
        for c in range(BOARD_COLUMNS):
            # to print the numbers horizontally above columns
            print(f"  ({c + 1}) ", end="")
        print("\n")

        # Printing the slots of the board
        for r in range(BOARD_ROWS):
            print('|', end="")
            for c in range(BOARD_COLUMNS):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n")
        print(f"{'-' * 43}\n")

    def player_turn(self):
        players = ["X", "O"]
        # This will alternate turns between players
        return players[self.turns % 2]

    def turn(self, column):
        # Search for an open slot starting form the bottom up till the first row and subtracting one every loop
        for r in range(BOARD_ROWS - 1, -1, -1):
            if self.board[r][column] == ' ':  # checks if the that place is empty
                self.board[r][column] = self.player_turn()  # execute the turn
                self.final_move = [r, column]
                self.turns += 1
                return True
        return False  # if the column is totally full

    def coordinate(self, r, c):
        #  tests if the row/column coordinate is in bounds of the created board to decide if it's a valid move
        # returns a boolean value
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLUMNS)

    def winner(self):
        last_row = self. final_move[0]
        last_column = self.final_move[1]
        last_letter = self.board[last_row][last_column]

        """ searching in [row, column] direction to find matching letter """

        directions = [[[-1, 0], 0, True],  # check above
                      [[1, 0], 0, True],  # check  down
                      [[0, -1], 0, True],  # check left
                      [[0, 1], 0, True],  # check right
                      [[-1, -1], 0, True],  # check diagonally
                      [[1, 1], 0, True],  # check diagonally
                      [[-1, 1], 0, True],  # check diagonally
                      [[1, -1], 0, True]]  # check diagonally

        # Search outwards tracking the matching pieces
        for a in range(4):
            for d in directions:
                """ this will shift the last move 'last row' and 'last column' 
                 by value of matching direction """
                r = last_row + \
                    (d[0][0] * (a + 1)
                     )  # a+1 is how many pieces we are searching outwards
                c = last_column + (d[0][1] * (a + 1))

                if d[2] and self.coordinate(r, c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:
                    # Stop searching in this direction if the letters are not matching
                    d[2] = False

        # Check possible direction pairs for '4 pieces in a row'
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i + 1][1] >= 3):
                self.print_board()
                print(f"{last_letter} is the winner!")
                return last_letter

        # No winners yet
        return False


def play_game():
    """to use the board we made , we will create a function to assign the class to a variable
              so we can use the former functions we created in that class"""
    game = Board()
    game_over = False
    while not game_over:
        game.print_board()  # printing the board as long as the game is not over
        # takes input from user as long as the game is not over and the input is acceptable
        possible_move = False
        while not possible_move:
            player_move = input(
                f"{game.player_turn()}'s Turn - choose a number from (1 : 7 ): ")

            if player_move.isdigit() == True and int(player_move) != 0:
                try:
                    possible_move = game.turn(int(player_move) - 1)
                except:
                    # warns the user on entering worng input
                    print(" WRONG INPUT , Please choose a number from 1 to 7 ")

        """ we will get a boolean return from the 'winner'
         so if it is false 'game over' will be false too and the loop goes on 
        and when ' winner' returns true the game will stop"""
        game_over = game.winner()

        # End the game if there is a tie
        if not any(' ' in x for x in game.board):
            print("..it is a tie..")
            return


if __name__ == '__main__':  # this line will keep the function paly_game running as long as the program is running too
    play_game()
