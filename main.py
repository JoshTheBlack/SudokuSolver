# Project to solve unique sudoku's programmatically.
# Assumes a provided sudoku has a unique solution

board = [[8,0,0,9,0,2,6,0,3],[1,2,4,8,0,3,0,0,0],[6,0,0,0,4,0,8,1,0],[7,0,1,6,0,0,0,0,9],[3,0,8,0,0,0,4,0,7],[0,0,0,4,0,9,0,3,8],[0,8,0,2,0,0,0,7,0],[0,0,3,0,8,6,0,5,4],[0,7,2,0,5,0,0,8,0]]

def printBoard(board):
    for row in board:
        if board.index(row) % 3 == 0:
            print("- - - - - - - - - - - - -")
        for i in range(len(row)):
            if i % 3 == 0:
                print("| ", end="")
            print(f"{row[i]} ", end="")
        print("|")

printBoard(board)