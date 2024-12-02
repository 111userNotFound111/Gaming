"""
226.Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# invert the existing binary tree 
# for each node:
#       swapping node.left and node.right
def invertTree(root):
    # base case 
    if not root:
        return 
    # initialise the first node
    node = root
    
    # swap the left and right pointer 
    left_temp = node.left
    node.left = node.right
    node.right = left_temp
    
    # move to the next pointer using recursion 
    invertTree(node.left)
    invertTree(node.right)
    
    return root

if __name__ == "__main__":
    invertTree()

