""" 

138. Copy List with Random Pointer


A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.


""" 

class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Create A Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        if not self.head:
            self.head = LinkedListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = LinkedListNode(value)
    
    def display(self):
        nodes_list = []
        current = self.head
        while current:
            nodes_list.append(current.val)
            current = current.next
        print(" -> ".join(map(str,nodes_list)))

    def returnHead(self):
        if self.head:
            return self.head

def listToLinkedList(input_list):
    # Initialize the head of the node 
    res_list = LinkedList()
    for item in input_list:
        res_list.insert(item[0])
    return res_list

input_list = [[7,'null'],[13,0],[11,4],[10,2],[1,0]]
linked_list = listToLinkedList(input_list)
linked_list.display()

############################ For 138. Copy List with Random Pointer ############################
# For Node with random
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    # use Two Pass Algorithm to construct the New Linked List with .random property
    # create hasmapping structure to store deepcopy of the linkedlist
    # structure of deep copy = { oldNode : newNode }
    deepCopy = {None : None}

    # 1st Pass 
    # construct new node based on old node values 
    current = head
    while current:
        copy = Node(current.val)
        deepCopy[current] = copy
        current = current.next
    
    # 2nd Pass
    # Add reference to connect the new pointers
    # reinitialize pointer 
    current = head
    while current:
        copy = deepCopy[current]
        copy.next = deepCopy[current.next]
        copy.random = deepCopy[current.random]
        current = current.next

    return deepCopy[head]