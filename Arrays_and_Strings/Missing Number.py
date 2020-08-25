"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Solution: For each number set nums[num]*=-1
          Then check the numbers to see if any index has positive or zero value.
          Special cases for 0 and n.
          Time complexity : O(N)
          Space complexity : O(1)

          Use expected sum - actual sum (n(n+1)/2 -> expected sum)
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = False
        zero = False
        for num in nums:
            if abs(num) == len(nums):
                n = True
                continue
            nums[abs(num)] *=-1
            if nums[abs(num)] == 0:
                zero = True
        #print(nums, n)
        for idx, num in enumerate(nums):
            if num >= 0:
                if num == 0 and not zero:
                    return idx
                elif num != 0:
                    return idx
        if n:
            return 0
        else:
            return len(nums)

s = Solution()
print(s.missingNumber([3,0,1]))
        
