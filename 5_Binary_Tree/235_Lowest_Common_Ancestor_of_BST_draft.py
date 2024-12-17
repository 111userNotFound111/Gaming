"""
235 Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

"""


import Binary_Tree


# LCA node: p and q are direct sub-node of LCA
# LCA node can be either p and q 
class Solution:
    def lowestCommonAncestor(self, root, p, q ):
        # Base case: if the current node is None, p, or q, return it
        if not root or root == p or root == q:
            return root
        
        # Recursively search the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are not None, this is the LCA
        if left and right:
            return root
        
        # Otherwise, return the non-null child
        return left if left else right
        
if __name__ == "__main__":
    test_list = [6,2,8,0,4,7,9,None,None,3,5]
    p = 2
    q = 8
    BTree = Binary_Tree.BinaryTree()
    BTree.insertList(test_list)
    print(BTree.head.val)
    solution = Solution()
    output = solution.lowestCommonAncestor(BTree.head,p,q)
    print(output)