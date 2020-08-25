"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Similar to container with most water, for each point, find the leftmax and right max for that point.

Once all the values are calculated, water at any point is min(left,right) - height[i] if the value is positive

Time complexity : O(N)
Space complexity : O(N)

"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = [0]*len(height)
        right = [0]*len(height)
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i-1])
        for j in range(len(height)-2, -1, -1):
            right[j] = max(right[j+1], height[j+1])
        for i in range(len(height)):
            l = left[i]
            r = right[i]
            if (min(l,r)-height[i]) > 0:
                ans += (min(l,r)-height[i])
        return ans

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))