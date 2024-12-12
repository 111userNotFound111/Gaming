"""

572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.


"""

import Binary_Tree

# check if subRoot tree is a sub tree of root tree
class Solution:
    def isSubtree(self, root, subRoot):
        
        # base case
        if root == None:
            return False
        
        if subRoot == None:
            return True
        
        print(f"current root {root.val}")
        
        # if found the the subRoot tree's head node in Root tree 
        if self.isSameTree(root, subRoot):
            return True
        
        # recursive case
        is_sub_tree = self.isSubtree(root.left, subRoot)
        if is_sub_tree == True:
            return True
        
        is_sub_tree = self.isSubtree(root.right, subRoot)
        if is_sub_tree == True:
            return True

        return False
    
    # check all nodes in root and subRoot for same Tree
    def isSameTree(self, root, subRoot):
        
        # check node structures 
        if root == None and subRoot == None:
            return True
        # one of them is None
        if root == None or subRoot ==None:
            return False

        if root and subRoot:
            if root.val == subRoot.val:
                if self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right):
                    return True

        return False
        
if __name__ == "__main__":
    solution = Solution()
    root_list = [3,4,5,1,2]
    subRoot_list = [4,1,2]
    root_binary_tree = Binary_Tree.BinaryTree()
    subRoot_list_tree = Binary_Tree.BinaryTree()
    root_binary_tree.insertList(root_list)
    subRoot_list_tree.insertList(subRoot_list)
    res = solution.isSubtree(root_binary_tree.head, subRoot_list_tree.head)
    print(res)