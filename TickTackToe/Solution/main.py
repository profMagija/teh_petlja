import numpy as np

C_ROWS = 3
C_COLS = 3
EMPTY_SYMBOL = ' - '

#? Used to map 2D coordinates to 1D array we use for board representation
BOARD_FIELDS = {
    (0, 0) : 0,
    (0, 1) : 1,
    (0, 2) : 2,
    
    (1, 0) : 3,
    (1, 1) : 4,
    (1, 2) : 5,
    
    (2, 0) : 6,
    (2, 1) : 7,
    (2, 2) : 8
}


def display_welcome_message():
    """
    Displays welcome message for the players.
    """
    print("Welcome to the awesome tick-tack-toe game simulator, I hope you'll have fun!")

def get_player_names():
    """
    Gets and returns player names as a tuple.
    First element in the tuple is the name of the first player.
    Second element in the tuple is the name of the second player.
    """
    first_player = input("Please input the name of the first player: ")

    second_player = input("Please input the name of the second player: ")

    return first_player, second_player

def construct_board():
    """
    Creates empty tick-tack-toe board

    It returns it as a matrix of strings.
    """

    #? We will construct board as array of strings, because it's the easiest way to do it
    board = []
    
    i = 0
    while i < C_ROWS * C_COLS:
        board.append(EMPTY_SYMBOL)
        i += 1

    return board

def create_signs(first_player, second_player):
    """
    Creates and returns dictionary which contains signs which players are using,
    it can be modifed to take custom signs.
    """

    signs = {}
    signs[first_player] = "X"
    signs[second_player] = "O"

    return signs

def print_board(board):
    """
    Prints the current board.
    """

    i = 0
    j = 0

    to_print = ""
    while i < C_COLS * C_ROWS:
        
        to_print += board[i]
        j += 1
        
        #? if the j is 3, we know that we must go to the new row
        if j == 3:
            to_print += "\n"
            j = 0        
        
        i += 1

    print(to_print)

def make_input(board, player, player_sign):
    """
    Asks the player for input, check if the input is correct and update the board if it is.

    Returns the col and row players has input
    """
    #? This is used because we know that we have a square matrix, and that only
    #? valid cols and rows are those below, so this is the easiest solution
    valid_fields = ['0', '1', '2']

    #? We want to have them in the main scope so we can return their valid values
    row = ""
    col = ""

    valid_input = False
    while(not valid_input):

        player_input = input("Please input row and column, separated by space: ")
        player_input = player_input.split(" ")
        
        if(len(player_input) != 2): 
            print("You must enter 2 valid fields separated by space, try again")
            continue
        
        col = player_input[0]
        row = player_input[1]

        if((row not in valid_fields or col not in valid_fields)):
            print("You must enter 2 valid fields, try again")
            continue
        
        col = int(col)
        row = int(row)

        if board[BOARD_FIELDS[(row, col)]] != EMPTY_SYMBOL:
            print("That field already has an input, try again")
            continue
        
        valid_input = True
        board[BOARD_FIELDS[(row, col)]] = ' ' + player_sign + ' '

    return row, col

def tie(board):
    """
    Checks if the result is tied. This function is always called after
    win checking, so that we for sure know that there are no more fields to be field
    and that no one has won
    """
    all_filled = True
    
    #? Another way this loop can be done is to 
    #? go directly to values which corespond to
    #? dictionary keys.
    #? we can do that by typing: for key, value in dict.items(): do something
    for pos in BOARD_FIELDS:
        if(board[BOARD_FIELDS[pos]] == EMPTY_SYMBOL):
            all_filled = False

    return  all_filled

def check_win(board, col, row):
    """
    Checks if the player whose input was [col, row] has won, returns true or false
    """
    

def main():

    print(BOARD_FIELDS[(0, 0)])

    board = construct_board()
    print(board)
    print(board[BOARD_FIELDS[(0, 0)]])


    display_welcome_message()
    first_player, second_player = get_player_names()
    

    signs = create_signs(first_player, second_player)    
    print(signs)

    


    #? Initialization part here
    #? You need to display welcome message
    #? You need to ask players to enter their names
    #? You need to save those names for future use
    #? You need to construct empty 3x3 tick-tack-toe board

    #? Game loop and logic here. Loop must go on until it's a tie or one of the players has won
        
        #? Check if it's a tie
        
        #? Ask first player to choose a field 
        #? Check if the player has won

        #? Ask second player to choose a field 
        #? Check if the player has won
    
    #? When the game is finished, result is saved in /results folder
    #? IMPORTANT: Every pair of players must have his own .txt files (order of the players is irrelevant), player names are not case sensitive
    #? If the .txt file already exist, it must be updated with the new results
    #? Example file you can use as pattern (but you don't have to) is example_saved_data.txt

    #? Appropriate message is displayed after the game has finished (based on who won, or if it was a tie)
    #? After 'enter' key is pressed current game statistics are show in the following format:
        #? - Number of wins for the first player, win percentage of the first player
        #? - Number of wins for the second player, win percentage of the second player
        #? - Number of tied games, tie games percentage
        #? eg. if there was 4 games and first player won 2, second won 1, and the 1 was tied the the output would be
            #? first_player_name: 2 wins, 50% of all games
            #? second_player_name: 1 win, 25% of all games
            #? Number of tied games: 1, 25% of all games
            #? Keep in mind that your generated sentences must be grammatically correct
        #? After this there is an additional message which asks the players if they want to play another game or they want to quit
        #? If they want to play another game, everything except welcome message is repeated
        #? If they want to exit, program displays goodbye message and finishes
        
    

if __name__ == "__main__":
    main()