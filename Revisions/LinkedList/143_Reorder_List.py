"""

input : singly list 

output : reordered singly list 

L0 → L1 → … → Ln - 1 → Ln

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

use two pointer method (slow, fast pointer)

to find mid, the slow fast pointer relation should be 
slow = x 
fast = 2x
constaint fast and fast.next should both exist ( for linked list odd and even )

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
    
    
def Convert_List_To_Linked_List(input_list):
    linked_list = LinkedList()
    for node in input_list:
        linked_list.insertNode(int(node))
    return linked_list

def reorderList(head):
    if head:
        slow = head
        fast = head.next

        if fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the entire list
        second = slow.next

        # break the orignal linked list from slow pointer (middle)
        prev = None
        slow.next = None

        while second:
            pointer_to_next = second.next
            second.next = prev
            prev = second
            second = pointer_to_next
        
        # merge both first and asecond linked list 
        first, second = head, prev

        while second:
            temp1 , temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
            



if __name__ == "__main__":
    input_list = [1,2,3,4]
    linked_list = Convert_List_To_Linked_List(input_list)
    reordered_list = LinkedList()
    reordered_list.head = linked_list.head
    reordered_list = reorderList(reordered_list.head)



