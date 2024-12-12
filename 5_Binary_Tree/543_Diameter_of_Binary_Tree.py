"""

543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

"""
import Binary_Search_Tree

# longest path between any two nodes 
# the longest path exists between two endpoints:
    # case 1: from leaf node to leaf node
    # case 2: from leaf node to root node
class Solution:
    def diameterOfBinaryTree(self, root) :
        # only list is mutable within another function
        # or can use self.longest_path (class property)
        longest_path = [0]
        self.findLongestPath(root, longest_path)
        
        return longest_path[0]

    def findLongestPath(self,node,longest_path):        
        if node is None:
            return 0
        
        # get the total distance from left and right leaf to the current node
        leftPath = self.findLongestPath(node.left, longest_path)
        rightPath = self.findLongestPath(node.right, longest_path)
        # the longest path is the sum of left and right path 
        current_path = leftPath + rightPath
        # update the path if its greater than current longest 
        if current_path > longest_path[0]:
            longest_path[0] = current_path
            
        return max(leftPath, rightPath)+1


if __name__ == "__main__":
    solution = Solution()
    input_list = [1,2,3,4,5]
    bst = Binary_Search_Tree.BTS()
    for num in input_list:
        bst.insertion(num)
    
    print(solution.diameterOfBinaryTree(bst.head))