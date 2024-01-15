"""

143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# not creating a new list but only modify the existing one
def reorderList(head):
    # Find mid of linked list 
    slow , fast = head, head.next
    # the last position of slow pointer is mid
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second part of list
    # change slow.next reference to none
    prev = slow.next = None
    second = slow.next
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # re-arrange the list
    first, second = head, prev
    # second is the shorter list
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2






if __name__ == "__main__":
    reorderList()