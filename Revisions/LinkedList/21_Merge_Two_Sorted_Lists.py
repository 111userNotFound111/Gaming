"""

input : heads of 2 SORTED linked lists

operation : merge into one SORTED linked list

output : head of one SORTED linked list

use two pointer method on the two linked lists

compare the current nodes:
    if both pointers exists 
    the smaller one is the next node, move to next
    if same, either can be next, both pointer move to next
    if one pointer is none 
    add the other pointer to the linked list, move next

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

# list1 and list2 are the head of linkedlist1 and 2
def merge_list(list1, list2):
    # create a new var to store the reference
    dummy = ListNode(None)
    tail = dummy
    
    # two pointer method 
    # either pointer exists
    while list1 and list2:
        # if both pointer exists
        if list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
    # if one of the pointer does not exist, 
    # linked the tail to the remaining of the existing list
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    # store the first val of the new linked list as head
    head = dummy.next
    return head

if __name__ == "__main__":
    input_list1 = [1,2,4]
    input_list2 = []
    linked_list1 = Convert_List_To_Linked_List(input_list1)
    linked_list2 = Convert_List_To_Linked_List(input_list2)
    linked_list1.display()
    linked_list2.display()

    merge_head = merge_list(linked_list1.head, linked_list2.head)
    merged_list = LinkedList()
    merged_list.head = merge_head
    merged_list.display()