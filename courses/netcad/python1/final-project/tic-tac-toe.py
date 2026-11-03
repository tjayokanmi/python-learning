board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, "O"]
]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print("+-------+-------+-------+")
        for column in row:
            print(f"|   {column}   ", end="")
        print("|")
    print("+-------+-------+-------+")


# def enter_move(board):
#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.
    result = []
    for row_index, row in enumerate(board):
       for column_index, column in enumerate(row):
            position = (row_index, column_index)
            if isinstance(column, int):
                result.append(position)  
    return result 

# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.

print(make_list_of_free_fields(board))