# create a binary search tree

class TreeNode:
    def __init__(self,value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
class BTS:
    def __init__(self):
        self.head = None
    
    def insertion(self, val):
        newNode = TreeNode(val)
        if not self.head:
            self.head = newNode
        else:
            currentNode = self.head

            while True:
            # check if the inserted node value is smaller or greater than the current node
            # move to left if val is smaller than current Node
                if val < currentNode.val:
                    if currentNode.left:
                        currentNode = currentNode.left
                    # connect current leaf node with the new node
                    else:
                        currentNode.left = newNode
                        break
            # move to right if val is greater than current Node
                else:
                    if currentNode.right:
                        currentNode = currentNode.right
                    # connect current leaf node with the new node
                    else:
                        currentNode.right = newNode
                        break

    def insertList(self, input_list):
        for num in input_list:
            self.insertion(num)
        
    # check if a value is in the Tree:
        # return true if value exist, otherwise return false             
    def find(self, val):
        # if BST is empty return false 
        if self.head == None:
            return False 
        # initialise a new pointer to traverse in BST
        currentNode = self.head
        
        # iterations 
        while currentNode:
            if currentNode.val == val:
                return True
            elif val > currentNode.val:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
                
        return False
    
if __name__ == "__main__":
    input_list = [4,2,1,3,6,5,7]
    binary_search_tree = BTS()
    binary_search_tree.insertList(input_list)
    res = binary_search_tree.find(10)
    print(res)
