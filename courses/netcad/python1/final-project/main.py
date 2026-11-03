import random

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
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


def enter_move(board):
#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.
    
    while True:
        try:
            print("make a move: Select a number from 1 to 9")
            move = int(input("> "))
            if 1 <= move <= 9:
                row_index = (move -1)//3
                column_index = (move-1) % 3
            else:
                print("Number is out of range")
                continue
            if board[row_index][column_index] in ["O", "X"]:
                print("The cell is occupied. Choose a free cell.")
                continue

            board[row_index][column_index] = "O"
            break
        except ValueError:
            print("Invalid Input: kindly enter a number between 1 and 9")
    

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

def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game
    for row in range(3):
        if (board[row][0] == sign and 
            board[row][1] == sign and 
            board[row][2] == sign):
            return True

    for column in range(3):
        if (board[0][column] == sign and 
            board[1][column] == sign and
            board[2][column] == sign):
            return True
    if (board[0][0] == sign and 
        board[1][1] == sign and 
        board[2][2] == sign):
        return True
    
    if (board[0][2] == sign and 
        board[1][1] == sign and 
        board[2][0] == sign):
        return True
        
    return False

def draw_move(board):
#     # The function draws the computer's move and updates the board.
    
    positions = make_list_of_free_fields(board)
    selected = random.choice(positions)
    row_index, column_index = selected
    board[row_index][column_index] = "X"
    # while True:
    #     number = random.randint(1,9)
    #     row_index = (number -1)//3
    #     column_index = (number-1) % 3
    #     if board[row_index][column_index] in ["O", "X"]:
    #         continue
    #     board[row_index][column_index] = "X"
    #     break

def main(board):
    display_board(board)
    board[1][1] = "X"
    display_board(board)
    while True:
        enter_move(board) 
        if victory_for(board,"O"):
            print("The user has Won!")
            display_board(board)
            break
        if not make_list_of_free_fields(board):
            print("The board is full without a winner: Draw!")
            display_board(board)

            break
        draw_move(board)
        display_board(board)
        if victory_for(board,"X"):
            print("The computer has won!")
            display_board(board)

            break
        if not make_list_of_free_fields(board):
            print("The board is full without a winner: Draw!")
            display_board(board)
            break

main(board)