"""
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
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

    def removeNthFromEnd(self, head, n):
        if head == None:
            return []
        first = head
        counter = 0
        while counter != n:
            second = first.next
            first = first.next
            counter += 1
        if second.val == None or first.val == None:
            return []
        else:
            prev = first
            while second.next != None:
                prev = first
                first = first.next
                second = second.next
            
            prev.next = first
            
            

    
def Convert_List_To_Linked_List(input_list):
    linked_list = LinkedList()
    for node in input_list:
        linked_list.insertNode(int(node))
    return linked_list

if __name__ == "__main__":
    input_list = [1,2,3,4,5]
    linked_list = Convert_List_To_Linked_List(input_list)
    linked_list.display()
