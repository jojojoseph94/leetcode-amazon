"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Iterative : iterate over the list, keeping track of previous node.

None   1 ----> 2 ------>3 -----> None
prev  node     temp
None <--1      2-------->3------>None
       prev   node      temp
None <--1 <----2        3------->None
              prev     node      temp

Recursive : Recursively travel till tail of list and return that new_head
            Reversal code
            current.next.next = current
            current.next = None

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head