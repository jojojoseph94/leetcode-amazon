"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Solution : Bruteforce : 3 loops and check if sum amounts to zero. O(N^3). TLE
    no sort 2 sum - reduce the problem to 2 sum over a loop. At each point check if the complement value is there
                    in the seen dictionary. Add a dups set to avoid processing duplicate elements.
                    time complexity : O(N^2)
                    space complexity : O(N)
    sorted 2 sum - sort the nums and over a loop use left and right pointers to find sum of iterating element, left and right.
                   advance at each point based on the sum. 
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # no sort solve using 2 sum
        ans = set()
        dups = set()
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i+1, len(nums)):
                    val = -(nums[i] + nums[j])
                    if val in seen and seen[val] == i:
                        ans.add(tuple(sorted([nums[i], nums[j], val])))
                    seen[nums[j]] = i
        return ans
    
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        # sort and solve using 2 sum II
        ans = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i==0 or nums[i] != nums[i-1]:
                lo = i +1
                hi = len(nums)-1
                while lo < hi:
                    if nums[i] + nums[lo] + nums[hi] == 0:
                        ans.add((nums[i], nums[lo], nums[hi]))
                        lo+=1
                        hi-=1
                    elif nums[i] + nums[lo] + nums[hi] > 0:
                        hi-=1
                    else:
                        lo+=1
        return ans

s = Solution()
print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))