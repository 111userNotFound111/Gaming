"""

A DFS traversal of a balanced BST

Aim: traverse a balanced BST and create a sorted list based on this BST (from small to large value)

"""

import Binary_Search_Tree

# Depth First Search uses Recursions to find the end values
def DFS_sort(node):
    def dfs_helper(node, sorted_list):
        # base case
        if node == None:
            return
        # recursive case
        # DFS all the left elements first 
        DFS_sort(node.left)
        # append the current value before traverse to the right
        sorted_list.append(node)
        # traverse to the right
        DFS_sort(node.right)
    
    sorted_list = []
    dfs_helper(node, sorted_list)