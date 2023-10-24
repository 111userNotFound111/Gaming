"""
206. Reverse Linked List (Reversing one direction link list)

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# create linked list node struct
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# create linklist functionality
class LinkedList:
    def __init__(self):
        self.head = None
    # insert node to linked list 
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    # print method for linked list
    def printLL(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
        print("None")

# reverse linked list 
# 1. get the current node 
# 2. construct two new variables:
    # prev : store the address of the previous node 
    # curr : store the address of the next node
# 3. use dummy to store reference of current.next 
# 4. move to next node by accessing dummy variable
    def reverseList(self):
        head = self.head
        prev, curr = None, head
        # if node exists
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        return


if __name__ == "__main__":
    # construct a linked list
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)

    print("Original List:")
    ll.printLL()

    ll.reverseList()
    print("\nReversed List:")
    ll.printLL()