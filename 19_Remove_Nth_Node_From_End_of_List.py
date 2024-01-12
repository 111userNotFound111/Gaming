"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# use two pointer method to solve this question
# the spacing between 2 pointers  = n
def removeNthFromEnd(self, head, n):
    # initialize a new linked list 
    # use dummy head 
    dummy = ListNode(0,head)
    dummy.next = head
    spacing = n -1

    # use two pointer method 
    # initialize the two pointers 
    if head:
        first = dummy
        second = head
        # get the initial spacing of the two pointers
        while spacing > 0 :
            second = second.next
            spacing -= 1
    
    # start iteration 
    while second.next:
        first = first.next
        second = second.next
    
    # the nth node = left.next
    # delete nth node : set pointer to the next node after nth node
    first.next = first.next.next

    return dummy.next






