"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Solution : for O(N) complexity, use 2 lists to store products left of a number and right of a number. The product of the two is the ans
Given numbers [2, 3, 4, 5], regarding the third number 4, the product of array except 4 is 2*3*5 which consists of two parts: left 2*3 and right 5. The product is left*right. We can get lefts and rights:

Numbers:     2    3    4     5
Lefts:            2  2*3 2*3*4
Rights:  3*4*5  4*5    5      
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [1]*len(nums)
        bck = [1]*len(nums)
        for i in range(1,len(nums)):
            fwd[i]=fwd[i-1]*nums[i-1]
            bck[len(nums)-i-1]=bck[len(nums)-i]*nums[len(nums)-i]
        for i in range(len(nums)):
            fwd[i]=fwd[i] *bck[i]
        return fwd

s = Solution()
print(s.productExceptSelf([1,2,3,4]))