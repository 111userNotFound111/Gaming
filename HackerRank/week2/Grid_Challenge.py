"""
Given a square grid of characters in the range ascii[a-z], 
rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, top to bottom. 
Return YES if they are or NO if they are not.

"""


# rearrange row in aphabetically
# check if the columns are also in ascending order

# function that rearrange the row in aphabetical order
def rearrangeGrid(grid):
    grid_list = []
    for string in grid:
        string_list = [x for x in string]
        string_list.sort()
        grid_list.append(string_list)
    return grid_list

# chekc if columns are also in ascending order 
def gridChallenge(grid):
    sorted_gird = []
    sorted_gird = rearrangeGrid(grid)
    
    # comparing the char in the list with the char in previous list 
    for row_index in range(1,len(sorted_gird)):
        for column_index in range(0, len(sorted_gird[0])):
            ascii_cur = ord(sorted_gird[row_index][column_index])
            ascii_prev = ord(sorted_gird[row_index-1][column_index])
            
            if ascii_cur < ascii_prev:
                return "NO"
            
            
    return "YES"


if __name__ == "__main__":
    input_grid =['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    print(gridChallenge(input_grid))