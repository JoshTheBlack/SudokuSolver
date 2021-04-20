# Project to solve unique sudoku's programmatically.
# Assumes a provided sudoku has a unique solution
from typing import DefaultDict

board = [[8,0,0,9,0,2,6,0,3],[1,2,4,8,0,3,0,0,0],[6,0,0,0,4,0,8,1,0],[7,0,1,6,0,0,0,0,9],[3,0,8,0,0,0,4,0,7],[0,0,0,4,0,9,0,3,8],[0,8,0,2,0,0,0,7,0],[0,0,3,0,8,6,0,5,4],[0,7,2,0,5,0,0,8,0]]
board2 = [[6,0,0,0,0,1,0,0,9],[0,0,0,0,3,0,6,0,0],[4,0,0,0,0,0,7,0,0],[8,0,0,0,0,0,0,9,0],[0,0,0,0,0,8,0,5,3],[0,2,0,7,0,3,0,0,1],[0,0,0,6,8,0,0,0,0],[0,9,0,0,0,0,0,0,0],[0,1,0,0,0,7,0,2,0]]


def printBoard(board):
    for row in board:
        if board.index(row) % 3 == 0:
            print("- - - - - - - - - - - - -")
        for i in range(len(row)):
            if i % 3 == 0:
                print("| ", end="")
            print(f"{row[i]} ", end="")
        print("|")

def findNextCell(board):
    d = DefaultDict()
    for x in range(1,len(board)+1):
        for y in range(1,len(board)+1):
            if board[x-1][y-1] != 0: continue
            sees = whatCellSees(board, (x,y))
            count = len(sees)
            d[(x,y)] = [count, sees]
    try:
        return sorted(d.items(),key=lambda kv: kv[1], reverse=True)[0]
    except:
        return None, None

def whatCellSees(board,cell):
    d = DefaultDict(int)
    x,y = cell
    for cell in board[x-1]:
        if cell != 0:
            d[cell] += 1
    for i in range(len(board)):
        if board[i][y-1] != 0:
            d[board[i][y-1]] += 1
    xmod = (x-1) // 3
    ymod = (y-1) // 3
    for i in range(xmod*3, xmod*3+3):
        for j in range(ymod*3, ymod*3+3):
            if board[i][j] != 0:
                d[board[i][j]] += 1
    return sorted(d)

def solve(board):
    find = findNextCell(board)
    if not find[0]:
        return True
    cell, sees = find
    for i in range(1,10):
        if i in sees[1]: continue
        board[cell[0]-1][cell[1]-1] = i
        if solve(board):
            return True
        board[cell[0]-1][cell[1]-1] = 0
    return False

solve(board2)
printBoard(board2)
#print(whatCellSees(board,(1,8)))

    