"""

100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""

import Binary_Tree

# check if two binary trees are structurally identical, and nodes have the same value 
class Solution:
    def isSameTree(self, p, q):

        # check node structures 
        if p == None and q == None:
            return True
        # one of them is None
        if p == None or q ==None:
            return False

        if p and q:
            if p.val == q.val:
                if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                    return True

        return False

        

# this does not work in local as the tree given in the question is not BST 
# check answer in leetcode
if __name__ == "__main__":
    solution = Solution()
    p = [1,2]
    q = [1,None,2]
    p_tree = Binary_Tree.BinaryTree()
    p_tree.insertList(p)
    q_tree = Binary_Tree.BinaryTree()
    q_tree.insertList(q)
    res = solution.isSameTree(p_tree.head, q_tree.head)
    print(res)