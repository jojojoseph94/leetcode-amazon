"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

Solution : Sort the numbers. Use 2 pointers at each iteration and to find the sum and then check if its closer.
            Move the pointers based on the sum value being greater or less than target
            Time complexity : O(N^2)
            Space complexity : O(1)
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = -(2**31)
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums)-1
            while lo < hi:
                if nums[i] + nums[lo] + nums[hi] == target:
                    return target
                if abs(target - (nums[i] + nums[lo] + nums[hi])) < abs(target - ans):
                    ans = (nums[i] + nums[lo] + nums[hi])  
                if (nums[i] + nums[lo] + nums[hi]) < target:
                    lo +=1
                else:
                    hi-=1
        return ans

s = Solution()
print(s.threeSumClosest([0,2,1,-3], 1))