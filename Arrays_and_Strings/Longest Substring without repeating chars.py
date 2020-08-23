"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution
Bruteforce : generate all substrings O(N^2). For each substring if all chars in that substring is uniq.
             If yes, check if its greater than ans.
             Time complexity : O(N^3)
             Space complexity: O(min(m,n)) -> for dict m is size of charset
             Time Limit exceeded

Optimization : iterate from left to right keeping track of indexes and chars in a dict.left, right will initially be zero.
                If a char which previously occurred is encountered, change left to left or index next to previous occurence of that char
                whichever is higher. 
                Example abba -> At index 4, we already have a in dict at index 0, but left is already at index 3, so left can be the same.

                length will be right-left+1 at every point
            Time complexity : O(N)
            Space complexity : O(min(m,n)) m is size of charset
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        dict_ = {}
        left = 0
        right = 0
        for index, char in enumerate(s):
            if char in dict_:
                left = max(left, dict_[char] + 1)
                dict_[char] = index
            else:
                dict_[char] = index
            right = index
            ans = max(right-left+1, ans)
        return ans

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))