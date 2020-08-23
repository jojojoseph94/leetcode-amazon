"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Solution : Bruteforce -> for each height, check area with every other height to the right, check if its greater than ans.
                         Time complexity : O(N^2)
                         Space complexity : O(1)
           optimized : start with left and right as 0 and last index. At each point, check area of water with ans.
            Move to the left or right, depending on which ever height is smaller. Continue till left or right cross each other.
            Time complexity : O(N)
            Sapce complextiy : O(1)
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height)-1
        while left <right:
            ans = max(ans, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return ans

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
