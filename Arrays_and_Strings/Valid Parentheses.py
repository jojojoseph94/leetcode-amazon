"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Solution : Use a stack to keep track of all opening brackets. Whenever a closing bracket is encountered,
 check the top of the stack to see if it has the same corresponding opening bracket.
 Time complexity : O(N)
 Space complexity : O(N)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(":")", "{": "}", "[":"]"}
        closing = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if stack:
                    ele = stack.pop(-1)
                    if closing[char] != ele:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True

s = Solution()
print(s.isValid("()[]{}"))