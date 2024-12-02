"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



"""

def lowestCommonAncestor(root, p, q):
    while root:
        # If both p and q are smaller than root, move to the left subtree
        if p.val < root.val and q.val < root.val:
            root = root.left
        # If both p and q are larger than root, move to the right subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            # This is the split point, so root is the LCA
            return root