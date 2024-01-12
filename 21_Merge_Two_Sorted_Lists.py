"""

21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

# create linked list node struct
class ListNode : 
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

# list1 : listNode 1
# list2 : listNode 2
def mergeTwoLists(list1, list2):
    # create a dummy node 
    # (create a dummy head and check if node exists)
    dummy = ListNode()
    tail = dummy

    # for case where at position p both listNode1 and listNode2 exists
    while list1 and list2:
        # compare node1 and node2
        # if node1 smaller than node2, insert node1 to new linkedlist 
        # move to next node in list1
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        # if node2 is smaller, insert node2 to new linkedlist
        # move to next node in list2
        else:
            tail.next = list2
            list2 = list2.next

        # move to the new tail node 
        tail = tail.next

    # if list1 and 2 are not equal length
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next

if __name__ == "__main__":
    print()