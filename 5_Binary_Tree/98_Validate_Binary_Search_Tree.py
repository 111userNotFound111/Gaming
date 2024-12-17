"""

98 Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

"""


import Binary_Tree
from collections import deque
# Aim : check if a binary tree is a BST: binary search tree
# all nodes on the left of sub tree should be smaller than current node
# all nodes on the right of sub tree should be greater than current node
# find a way to check if node 
class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        
        q = deque([(root, float("-inf"), float("inf"))])
        
        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))
        
        return True
    

if __name__ == "__main__":
    binary_tree = Binary_Tree.BinaryTree()
    test = [2,2,2]
    binary_tree.insertList(test)
    solution = Solution()
    print(solution.isValidBST(binary_tree.head))