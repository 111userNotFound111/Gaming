"""

36 Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""
from collections import defaultdict

# without using numpy
def isValidSudoku(board):
    # hash mapping struct
    # for row
    # {row_num : list [col_num] }
    row_dict = defaultdict(set)
    col_dict = defaultdict(set)

    # squre hashfunction:
    # {tuple(x,y):set{}}
    # where x = i // 3 , y = j // 3
    # x = 0 , 1 , 2   y = 0, 1, 2 
    square = defaultdict(set)

    for i in range(len(board)):
        for j in range(len(board)):
            cur_val = board[i][j]
            if cur_val == ".":
                continue
            if  (cur_val in row_dict[i] or 
                cur_val in col_dict[j] or 
                cur_val in square[(i//3,j//3)]): # use floor division as hash function
                return False
            else:
                row_dict[i].add(cur_val)
                col_dict[j].add(cur_val)
                square[(i//3,j//3)].add(cur_val)
    return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))