"""

110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false


"""

# find the depth to each node from the leaf node
# the challenge of this question is how to propagate the imbalance information back to the top of the recursion stack
# use a flag outside of the function to store the result (list or class property self - both are mutable within recursive function)
class Solution:
    def isBalanced(self, root):
        self.is_balanced = True
        self.checkBalanced(root)
        
        return self.is_balanced

    def checkBalanced(self, root):
        if root is None:
            return 0
        
        leftDepth = self.checkBalanced(root.left)
        rightDepth = self.checkBalanced(root.right)
        # check for height balance
        height_diff = abs(leftDepth - rightDepth)
        
        if height_diff>1:
            # use class property and save the flag directly 
            self.is_balanced = False
            
        
        return max(leftDepth, rightDepth) + 1
    
    
# cant not run here because the leetcode test case are not BST
if __name__ == "__main__":
    solution = Solution()
    output = solution.isBalanced()