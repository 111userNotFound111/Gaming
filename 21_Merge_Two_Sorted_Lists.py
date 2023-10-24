"""

21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

# create linked list node struct
class Node : 
    def __init__(self,data, next=None):
        self.data = data
        self.next = next
    
# create linked list struct
class LinkedList : 
    # initialise head 
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = Node(data)
        if self.head :
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode
        
    def printLinkedList(self):
        if self.head:
            curr = self.head
            while(curr):
                print(curr.data)
                curr = curr.next
            print("End")
                
if __name__ == "__main__":
    LL = LinkedList()
    LL.insert(1)
    LL.printLinkedList()