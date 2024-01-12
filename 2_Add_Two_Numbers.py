""" 

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

""" 



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        if not self.head:
            print(" Linked List does not exists ")
            return
        else:
            current = self.head
            while current:
                print(current.val)
                current = current.next
            print("End")
            
    def returnHead(self):
        return self.head

# list = [ node1, node2, node2 ]
def conver_list_to_linked_list(input_list):
    linked_list = LinkedList()
    for item in input_list:
        linked_list.insert(int(item))
    return linked_list



# 2 Edge Cases : 
#   1. L1 and L2 have different length 
#   2. Carry at the tail node creates a new node 
def addTwoNumbers( l1 , l2):
    # initialise head to the two linkedlist 
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2:
        # initialise val for both l1 and l2
        if l1:
            v1 = l1.val
        else : 
            v1 = 0 
        
        if l2:
            v2 = l2.val
        else :
            v2 = 0

        # starts the new calculations 
        sum = v1 + v2 + carry
        # reset carry after use 
        carry = 0
        # for next node carry 
        if sum >= 10:
            carry , val = divmod(sum, 10)
        
        # store sum value to new digit 
        l1 = l1.next
        l2 = l2.next 
        current.next = ListNode(val)

        # update nodes 
        current = current.next
        








if __name__ == "__main__":
    # testing functions 
    list1 = [2,4,3]
    list2 = [5,6,4]
    # convert list into linked list 
    linkedlist1 = conver_list_to_linked_list(list1)
    linkedlist2 = conver_list_to_linked_list(list2)
    # return head
    head1 = linkedlist1.returnHead()
    head2 = linkedlist2.returnHead()
    print(head1.val)
    # add two numbers 
    addTwoNumbers(head1, head2)
