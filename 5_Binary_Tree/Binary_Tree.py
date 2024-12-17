# this is just a binary tree not binary search tree
# simple binary tree : 
    # if root node is empty, insert new node to root 
    # from root node, check if left is empty, if empty insert new node
    # from root node, check if left is not empty, check if right is empty, if empty insert new node
    # if both left and right are not empty move to left node
    # fill the left node sub-tress, move to right node
    # none val are allowed which skips the pointer 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# use BFS 
class BinaryTree:
    def __init__(self):
        self.head = None

    
    def insert(self, val):
        newNode = TreeNode(val)
        if self.head == None:
            self.head = newNode
            return
        
        curNode = self.head
        nodeList = []
        
        # simple binary tree follows left and then right order
        # iterate condition: both left and right subtree exist, move to the next left
        while True:
            # do not link new val to None node
            if curNode == None:
                continue
            # prioritise link with left 
            if curNode.left:
                nodeList.append(curNode.left)
            else:
                # link new Node to leaf
                curNode.left = newNode
                return
            if curNode.right:
                nodeList.append(curNode.right)
            else:
                # link new Node to leaf
                curNode.right = newNode
                return
            
            # if no more nodes in the node list, stop the iteration 
            if len(nodeList) == 0:
                return 
            
            # iterate to the next node 
            curNode = nodeList.pop(0)
    
    def insertList(self, input_list):
        for num in input_list:
            self.insert(num)

    def _helper_dfs(self, node):
        if node == None:
            return 
        self._helper_dfs(node.left)
        print(node.val)
        self._helper_dfs(node.right)
    
    def _helper_bfs(self, node):
        queue = list()
        queue.append(node)
        
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    def display(self):
        self._helper_bfs(self.head)
        
if __name__ == "__main__":
    test_list = [3,9,20,None,None,15,7]
    binary_tree = BinaryTree()
    binary_tree.insertList(test_list)
    binary_tree.display()
            
            
            
            
            