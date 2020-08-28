"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        queue = collections.deque([root])
        flag = True
        while queue:
            level = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if flag:
                        level.append(node.val)
                    else:
                        level.appendleft(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                ans.append(level)
            flag = not flag
        return ans