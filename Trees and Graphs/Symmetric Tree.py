"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively
Recursive soln: recursive function which checks two nodes and if they are equal calls the recursive function again, but
on left subtree of first with right subtree of second and vice versa
Time complexity : O(N) -> all nodes are checked
Space complexity : O(N) -> recursive stack

Iterative : BFS with 2 queues, but order in which nodes are added to the queue are opposite in both queues.

"""

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                return symmetric(node1.left, node2.right) and symmetric(node1.right, node2.left)
            elif node1 or node2:
                return False
            else:
                return True
        return symmetric(root, root)
    
    def isSymmetricIterative(self, root: TreeNode) -> bool:
        queue1 = collections.deque([root])
        queue2 = collections.deque([root])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1 and node2:
                print(node1.val, node2.val)
                if node1.val != node2.val:
                    return False
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.right)
                queue2.append(node2.left)
            elif node1 or node2:
                return False
        if queue1 or queue2:
            return False
        else:
            return True