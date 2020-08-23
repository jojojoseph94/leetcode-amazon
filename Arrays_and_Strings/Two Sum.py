"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Soln: Bruteforce would be to check for each number, check if sum with any other number 
is target Time complexity : O(n^2) Space : O(1)

Optimized soln: Use a dict to keep track of numbers we already processed. 
For each number, check if the target-num is there in dict. If yes, then return the indexes

Time complexity : O(n) Space complexity : O(n)

"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            if target-num in num_dict:
                return [num_dict[target-num], index]
            else:
                num_dict[num] = index
        return -1

s = Solution()
print(s.twoSum([2,7,11,15], 9))