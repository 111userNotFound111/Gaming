"""

input : singly list 

output : reordered singly list 

L0 → L1 → … → Ln - 1 → Ln

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

use two pointer method 
two parts of the program 
spearate the orginal list into two parts cut from the middle 
reverse the last part 

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertNode(self, val):
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        
    def display(self):
        if self.head == None:
            print("linked list does not exists")
        else : 
            curr = self.head
            while curr:
                print(curr.val, end = ' -> ')
                curr = curr.next
            print("End")
    
    def returnHead(self):
        return self.head
    
    
def Convert_List_To_Linked_List(input_list):
    linked_list = LinkedList()
    for node in input_list:
        linked_list.insertNode(int(node))
    return linked_list