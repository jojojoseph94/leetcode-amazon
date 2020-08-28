"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node = head
        count = 0
        while node:
            node = node.next
            count+=1
        node = head
        tail = None
        new_head = None
        this_head = None
        prev_tail = None
        prev = None
        for _ in range(count//k):
            if not node:
                break
            for _ in range(k):
                temp = node.next
                if not tail:
                    tail = node
                node.next = prev
                this_head = node
                prev = node
                node = temp
            if prev_tail:
                prev_tail.next = this_head
            prev_tail = tail
            if not new_head:
                new_head = this_head
            prev = None
            tail = None
        #attach rest
        if node:
            prev_tail.next = node
        return new_head
                
            