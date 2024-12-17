"""

102 Binary Tree Level Order Traversal


Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]


Example 2:
Input: root = [1]
Output: [[1]]


Example 3:
Input: root = []
Output: []


Constraints:
0 <= The number of nodes in both trees <= 1000.
-1000 <= Node.val <= 1000

"""
import Binary_Tree


# BFS question that uses queue and dequeue
# Aim: return values of nodes at a particular level in the tree for all levels 

# use last_value to signal the break point 
# last_value are initialise as the last element in traversal_queue
class Solution:
    def levelOrder(self, root):
        # edge case : empty root 
        if root == None:
            return []
        # initialise variables
        traversal_queue=[root]
        last_node = traversal_queue[-1]
        level_list=[]
        output_list=[]
        
        # iteration
        # iterate only all nodes in the same level are added to the append list
        while traversal_queue:
            root = traversal_queue.pop(0)
            # add the current node to level list
            level_list.append(root.val)
            print(f"current node {root.val} and current level list {level_list}")
            
            # update iteration 
            if root.left:
                print(root.left.val)
                traversal_queue.append(root.left)
            if root.right:
                traversal_queue.append(root.right)
            
            # At last_value point
            if root == last_node:
                if traversal_queue:
                    last_node = traversal_queue[-1]
                output_list.append(level_list)
                level_list = []
                
        return output_list
    
    
if __name__ == "__main__":
    binary_tree = Binary_Tree.BinaryTree()
    input_list = [3,9,20,None,None,15,7]
    binary_tree.insertList(input_list)
    
    solution = Solution()
    res = solution.levelOrder(binary_tree.head)
    print(res)