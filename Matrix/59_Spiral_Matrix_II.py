"""

59.Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

"""
# generate an n x n matrix
# arranged from 1 to n^2 in spiral order
# spiral motion is right -> bot -> left -> top (repeat)
# use boundaries to signal motion changes
# update boundary pointers
class Solution:
    def generateMatrix(self, n):
        # initialise the spiral matrix
        spiral = [[0]*n for x in range(n)]
        # initialise boundary pointers
        left = 0
        right = n
        top = 0
        bot = n
        num = 1
        # there's case where left == right for odd number n 
        while num <= n*n:
            # left to right
            for j in range(left, right):
                spiral[top][j] = num
                num += 1
            top += 1
            
            # top to bot
            for i in range(top, bot):
                spiral[i][right-1] = num
                num += 1
            right -= 1
            
            # right to left
            # understand how range works here, python for loop follows [x,y) rule where include x but exclude y 
            for j in range(right-1,left-1,-1):
                spiral[bot-1][j] = num
                num += 1
            bot -= 1
            
            # bot to top
            for i in range(bot-1, top-1,-1):
                spiral[i][left] = num
                num += 1
            left += 1
        
        print(spiral)
        return spiral
        

if __name__ == "__main__":
    input_case = 3
    solution = Solution()
    solution.generateMatrix(input_case)