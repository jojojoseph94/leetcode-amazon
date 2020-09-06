"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

Solution : recursively call the function, with base case as root being null, or p or q; If so return root
            left = lcs(left subtree)
            right = lcs(right subtree)
            then if left subtree result is none, return right and vice versa.
            If both subtrees are not none, return root.
     7
    / \
   5   6
  / \
 1   3

 LCS of 1 and 3

     7         
    / \
   5   6   
  / \        
 1   3       
 
 at node 1 root is p so return 1, same for node 3
 at  5(LCS - left=1, right=3), SInce both subtrees are not none, return 5
 at 6(LCS - left=None, right = None), Hence LCS will be none
 at node 7, LCS left - 5, right = None, Hence left is returned (5)

 Time complexity : O(N)
 Space complexity : O(N) (Recursion stack)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root