"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

Solution : Create a dict with counts of characters in T.
           2 pointers, start and end both at zero. Loop over s, while end < len(s)
           Keep a dictionary to keep track of chars in the window.
           Over the iteration, keep track of if the string and if the string has been formed (using required_chars and formed_chars count)
           Once string is formed, move the start pointer one by one till the string is not formed any more. Then continue the loop.

           Time complexity : O(N)
           Space complexity : O(N)
"""

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = (float('inf'), None, None)
        if len(s) < len(t):
            return ""
        seen = {}
        for char in t:
            if char in seen:
                seen[char]+=1
            else:
                seen[char] = 1
        start = 0
        end = 0
        #why len(seen) instead of length of t?
        required = len(seen)
        formed = 0
        window_count = {}
        while end < len(s):
            char = s[end]
            window_count[char] = window_count.get(char, 0) + 1
            if char in seen and seen[char] == window_count[char]:
                formed+=1
            while formed == required and start <=end:
                char = s[start]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                window_count[char]-=1
                if char in seen and window_count[char] < seen[char]:
                    formed-=1
                start+=1
            end+=1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))