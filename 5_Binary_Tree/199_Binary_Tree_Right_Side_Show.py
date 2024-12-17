"""

199. Binary Tree Right Side View

You are given the root of a binary tree. 
Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:
Input: root = [1,2,3]
Output: [1,3]

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,7]

Constraints:
0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

"""

import Binary_Tree

# to show node viewed from right side 
# prioritise on right nodes 
# for each level of the tree, only one node can be seeing 
from collections import deque
class Solution:
    def rightSideView(self, root):
        # Edge case
        if root == None:
            return []
        # initialise a queue for BFS traversal
        # a level list to store all nodes in the same level
        # a res list to store results 
        q = deque([root])
        level = deque()
        res = [root.val]
        while q:
            node = q.popleft()
            print(f"node value {node.val}")
            if node.right:
                level.append(node.right)
            if node.left:
                level.append(node.left)
            
            if not q:
                # both q and level are empty means end of tree
                if not level:
                    break
                # add the first to the res
                res.append(level[0].val)
                # all nodes in current level become nodes traversed next
                q = level
                # empty level list
                level = deque()

        print(res)
        return res 
    
    
if __name__ == "__main__":
    binary_tree = Binary_Tree.BinaryTree()
    test = [1,2,3,None,5,None,4]
    binary_tree.insertList(test)
    solution = Solution()
    res = solution.rightSideView(binary_tree.head)
