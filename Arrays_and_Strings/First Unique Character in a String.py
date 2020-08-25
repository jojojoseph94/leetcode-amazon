"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.

Solution : Create counter for the string.
           Iterate over s from starting and check if count of that char is one.
        Time complexity : O(N)
        Space complexity : O(1) (26 chars only)
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for idx, char in s:
            if count[char] == 1:
                return idx
        return -1