"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

Solution : Keep a dictionary with key as number of occurance of each letter in the word. This lets us add the words that are anagrams
            under the same key

            Time complexity : O(N*M) -> N is the number of words, M being the length of the word
            Space complexity : O(N*M)

"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        ans = []
        for word in strs:
            key = [0]*26
            for letter in word:
                key[ord(letter)-ord('a')] +=1
            key = tuple(key)
            if key in dict_:
                dict_[key].append(word)
            else:
                dict_[key] = [word]
        for value in dict_.values():
            ans.append(value)
        return ans

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))