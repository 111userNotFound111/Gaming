"""

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current:
                current = current.next
            current = newNode
            
    def returnHead(self):
        return self.head

# use list (pos_list) to record every node's pointer / reference 
# if the node's reference already in list, its a cycle linked list and return true, else return false
class Solution:
    def hasCycle(self, head):
        pos_list = []
        node = head
        while node:
            if node not in pos_list:
                pos_list.append(node)
            else:
                return True
            node = node.next
        return False


def convert_list_to_LinkedList(input_list):
    linked_list = LinkedList()
    for item in input_list:
        linked_list.insert(int(item))
    return linked_list


if __name__ == "__main__":
    list1 = [3,2,0,4]
    list2 = [1,2,3]
    linkedList1 = convert_list_to_LinkedList(list1)
    linkedList2 = convert_list_to_LinkedList(list2)
    linkedList1_head = linkedList1.returnHead()
    linkedList2_head = linkedList2.returnHead()
    print(linkedList1_head.val)
    # solution = Solution
    # output = solution.hasCycle()