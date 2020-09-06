"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def backtrack(left,right, cur):
            if left+right == 2*n:
                self.res.append(cur)
                return
            if left < n:
                backtrack(left+1, right, cur + "(")
            if right < left:
                backtrack(left, right+1, cur + ")")
        backtrack(0,0,"")
        return self.res

s = Solution()
print(s.generateParenthesis(3))
