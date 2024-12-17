"""
1448 Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

"""

import Binary_Tree

# dfs to each leaf node
# find the Good nodes with current value greater than the max num traversed 
# compare current node value with max value traversed
# pass the result back from the recursive function
# understand how the count works in recursive function and how the answer is passed back to the top
class Solution:
    def goodNodes(self, root):
        good_nodes_count = self._dfs_helper(root, root.val)
        return good_nodes_count
    
    def _dfs_helper(self, node, max_value):
        
        # base case : return 0 if node not exist
        if not node:
            return 0
        
        # increment of count value
        if node.val >= max_value:
            count = 1
        else:
            count = 0
        
        # update max_value
        max_value = max(node.val, max_value)
        
        # recursive case: count the good nodes 
        count += self._dfs_helper(node.left, max_value)
        count += self._dfs_helper(node.right, max_value)
        
        # pass count back 
        return count
    
if __name__ == "__main__":
    test_list = [3,1,4,3,None,1,5]
    binary_tree = Binary_Tree.BinaryTree()
    binary_tree.insertList(test_list)
    solution = Solution()
    res = solution.goodNodes(binary_tree.head)