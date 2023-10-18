"""

74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""

# row is sorted in ascending order 
# check for pointer update condition

# use left and right to search target
# get the right mid value from row and col

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    # left : first element in the matrix
    left = 0
    # right : last element in the matrix
    right = (m * n) -1 

    while left <= right:

        mid = left + ((right - left) // 2)

        # get the exact value from mid 
        row = mid // n
        col = mid % n

        row_list = matrix[row]
        mid_val = row_list[col]

        if mid_val > target : 
            right = mid - 1

        elif mid_val < target :
            left = mid + 1
            
        else :
            return True
            
    
    return False
        

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(searchMatrix(matrix, target))
