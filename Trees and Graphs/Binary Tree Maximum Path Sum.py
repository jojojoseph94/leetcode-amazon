"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

Solution : Question is very similar to Diameter of binary tree
            At each level calculate local ans and compare with global ans.
            local ans is (L+node.val, R+node.val, L+R+node.val, node.val)
            return local ans at each level.
            Time complexity : O(N)
            Space complexity : O(N)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = None
        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            if self.ans == None:
                self.ans = L+R+node.val
            else:
                self.ans = max(self.ans, L+R+node.val, node.val, L+node.val, R+node.val)
            return max(node.val, L+node.val, R+node.val)
        dfs(root)
        return self.ans