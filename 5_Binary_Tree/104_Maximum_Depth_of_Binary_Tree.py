"""

    104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""
                


# update the search 
# DFS find the maxDepth 
# DFS: go to the leaf node, let leaf node as 0, +1 on return in recursion 

def maxDepth(root):
    if not root:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return max(left_depth, right_depth) + 1

if __name__ == "__main__":
    test_case = [1,2,3,None,None,4]
    res = maxDepth()