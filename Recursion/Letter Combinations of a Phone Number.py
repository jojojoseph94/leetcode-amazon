"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Solution : Recursive solution -> For each letter in in digit, explore all the paths recursively. This will give you all the combinations.
            Time complexity : O(3^Mx4^N) -> M 3 letter digits in input and N 4 letter digits (7,8,9)
            Space complexity : O(3^Mx4^N) -> Same since you have to keep that many solutions
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dig_len = len(digits)
        letter_dict = {"1":[""], "2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"], "8":["t","u","v"],"9":["w","x","y","z"]
        }
        def recurse(index, cur):
            if len(cur) > len(digits):
                return
            if len(cur) == dig_len:
                if cur:
                    res.append(cur)
                return
            for letter in letter_dict[digits[index]]:
                recurse(index+1, cur+letter)
        recurse(0,"")
        return res