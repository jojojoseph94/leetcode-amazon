"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Solution : Time complexity : O(N)
           Space complexity : O(N)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = None
        prev = None
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                if prev:
                    prev.next = node
                prev = node
                if not l3:
                    l3 = node
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                if prev:
                    prev.next = node
                prev = node
                if not l3:
                    l3 = node
                l2 = l2.next
        while l1:
            node = ListNode(l1.val)
            if prev:
                prev.next = node
            prev = node
            if not l3:
                l3 = node
            l1 = l1.next
        while l2:
            node = ListNode(l2.val)
            if prev:
                prev.next = node
            prev = node
            if not l3:
                l3 = node
            l2 = l2.next
        return l3