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
    def insert(self, val):
        newNode = Node(val)
        print('current head',self.head)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    # print method for linked list
    def printLL(self):
        if (self.head):
            current = self.head
            while(current):
                print(current.val)
                current = current.next
        else:
            print("Empty Linked List !")

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()