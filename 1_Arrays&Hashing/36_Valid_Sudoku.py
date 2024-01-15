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
    row_dict = defaultdict(list)
    
    # for col
    # {col_num: list [row_num]}
    col_dict = defaultdict(list)
    rep_set_col=set()

    # for 3x3


    # create a board 
    for i in range (0, len(board)):
        # check for row repetition
        rep_set_row=set()
        for j in range (0, len(board[i])):
            cur_val = board[i][j]
            if cur_val == ".":
                row_dict[i].append(0)
                col_dict[j].append(0)
            else:
                # check for case 1 : no repetition in row
                if cur_val not in rep_set_row and cur_val not in rep_set_col:
                    row_dict[i].append(int(cur_val))
                    rep_set_row.add(cur_val)
                    col_dict[j].append(int(cur_val))
                else:
                    return False

    # case 2: no repetition in col
    for col in col_dict.keys():
        #print("current column", col)
        rep_set_col=set()
        for row_num in col_dict[col]:
            #print("current value",row_num)
            if row_num ==0:
                continue
            if row_num not in rep_set_col:
                rep_set_col.add(row_num)
            else:
                return False
    
    # case 3 check for 3x3
    x_start=0
    y_start=0
    while True:
        rep_set_slide=set()
        x_end = x_start + 2
        y_end = y_start + 2

        # break case
        if  y_start == len(board):
                break
        
        for col in range(x_start,x_end+1):
            #print("current col", col)
            for row in range(y_start,y_end+1):
                #print("current row", row)
                if col_dict[col][row] == 0:
                    continue
                if col_dict[col][row] not in rep_set_slide:
                    rep_set_slide.add(col_dict[col][row])
                else:
                    return False

        # update x starting value
        x_start = x_end+1

        # update case
        if x_start == len(board):
                x_start = 0
                y_start = y_end+1


    # print("row dict", row_dict)
    # print("col dict", col_dict)
    return True

if __name__ == "__main__":
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))