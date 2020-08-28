"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Solution : Add numbers at each point keeping track of carry. At the end, if carry is still there, make a 
           linked list node for that.
           Time complexity : O(N)
           Space complexity : O(N)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = None
        prev = None
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val //10
            val = val %10
            node = ListNode(val)
            if prev:
                prev.next = node
            prev = node
            if not l3:
                l3 = node
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carry
            carry = val //10
            val = val %10
            node = ListNode(val)
            if prev:
                prev.next = node
            prev = node
            if not l3:
                l3 = node
            l1 = l1.next
        while l2:
            val = l2.val + carry
            carry = val //10
            val = val %10
            node = ListNode(val)
            if prev:
                prev.next = node
            prev = node
            if not l3:
                l3 = node
            l2 = l2.next
        if carry:
            node = ListNode(carry)
            if prev:
                prev.next = node
            prev = node
            if not l3:
                l3 = node
        return l3

s = Solution()
