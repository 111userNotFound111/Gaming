"""
Input : singly linked list 
Output : Reversed linked list 

Singly linked list are one directional 
1. Duplicate ppinter record current pointer to the next node 
2. change pointer point to previous node 
3. move to next node 


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# create linked list 
class LinkedList : 
    def __init__(self):
        self.head = None 
    
    def insertNode(self, value):
        node = ListNode(value)
        if self.head == None : 
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            # print("current node val ", node.val)
            current.next = node

    def reversed_list(self, head):
        if head == None : 
            print("linked list does not exist")
        else : 
            current = head
            prev_node = None
            while current:
                pointer_to_next = current.next
                current.next = prev_node
                prev_node = current
                current = pointer_to_next

            head = prev_node
            return head


    def display(self):
        current = self.head
        if current == None:
            print("Linked list does not exist")
        else:
            while current:
                print(current.val, end=" -> ")
                current = current.next
            print("End")

def Convert_List_To_Linked_List(input_list):
    linked_list = LinkedList()
    for node in input_list:
        print(node)
        linked_list.insertNode(int(node))
    return linked_list

                


if __name__ == "__main__":
    input_list1 = [1,2,3,4,5]
    linklist1 = Convert_List_To_Linked_List(input_list1)
    linklist1.display()


    reversed_head = linklist1.reversed_list(linklist1.head)
    reversed_list = LinkedList()
    reversed_list.head = reversed_head
    reversed_list.display()
