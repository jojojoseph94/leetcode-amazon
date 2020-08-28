"""
Given an array of linked-lists lists, each linked list is sorted in ascending order.

Merge all the linked-lists into one sort linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

Solution : Merge one by one -> O(k*N) time

Solution2: Divide and conquer - O(Nlog(k)) time
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #merge one by one
        if not lists:
            return None
        new_head = None
        for i in range(1,len(lists)):
            if new_head:
                list1 = new_head
            else:
                list1 = lists[0]
            list2 = lists[i]
            prev = None
            while list1 and list2:
                if list1.val < list2.val:
                    prev = list1
                    list1 = list1.next
                else:
                    temp = list2.next
                    list2.next = list1
                    if prev:
                        prev.next = list2
                    else:
                        new_head = list2
                    prev = list2
                    list2 = temp
            if list2:
                if prev:
                    prev.next = list2
                else:
                    new_head = list2
        if new_head:
            return new_head
        else:
            return lists[0]