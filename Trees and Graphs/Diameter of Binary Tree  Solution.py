"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

Solution : At each level calculate local maximum, which is the length of the subtree which passes through that node
           Compare that value to global ans.
           But return from each level the max of left or right answers plus one. This is because at one level above, the
           ans has to pass through that levels node.

          1      at level 2 this    But when coming to level one    
         / \     is the ans         this is the ans
        2   3       2                     1
       / \         / \                   /
      4   5       4   5                 2
                                       /
                                      4  

        Thats why we return max(L,R)+1 at each level
           Time complexity : O(N)

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return 0
        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L,R) + 1
        dfs(root)
        return self.ans-1