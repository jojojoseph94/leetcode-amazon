"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighs(i,j):
            n = [[i+x[0], j+x[1]] for x in [(-1,0),(0,1),(1,0),(0,-1)]]
            n_1 = []
            for k,l in n:
                if 0<=k<len(grid) and 0<=l<len(grid[0]) and grid[k][l] == "1":
                    grid[k][l] = "0"
                    n_1.append([k,l])
            return n_1
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ans+=1
                    grid[i][j] = "0"
                    queue = collections.deque()
                    queue.append([i,j])
                    while queue:
                        x,y = queue.popleft()
                        n = neighs(x,y)
                        if n:
                            for node in n:
                                queue.append(node)
        return ans
