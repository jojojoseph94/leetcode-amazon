"""
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
In one step you can walk in any of the four directions top, bottom, left and right also when standing in a point which is a tree you can decide whether or not to cut off the tree.

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

Constraints:

1 <= forest.length <= 50
1 <= forest[i].length <= 50
0 <= forest[i][j] <= 10^9

Solution : Sort the trees by height. (Consider only trees above height 1)
           Then starting from source as (0,0) do bfs to each tree in the sorted list. If path is available, add the number of steps 
           to the answer. Otherwise return -1.

           BFS may TLE at times if implementation is not super efficient.

           Time complexity : O(N*N*m)-> where m is the number of trees >1 and N*N is the grid size.
                             Space complexity : O(N)

"""

from typing import List
import collections

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(sr, sc, tr, tc):
            #finding number of steps to reach tr tc
            #from sr sc 
            ans = -1
            queue = collections.deque()
            queue.append([sr,sc,0])
            visited = {(sr,sc)}
            while queue:
                sr, sc, steps = queue.popleft()
                if sr == tr and sc == tc:
                    return steps
                neighs = [(sr,sc+1),(sr+1,sc),(sr-1,sc),(sr,sc-1)]
                for x,y in neighs:
                    if x>=0 and x<len(forest) and y>=0 and y<len(forest[0]) and forest[x][y] and (x,y) not in visited:
                            visited.add((x,y))
                            queue.append([x,y,steps+1])
            return -1
        
        trees = sorted((v,r,c) for r, row in enumerate(forest) for c,v in enumerate(row) if v > 1)
        ans = 0
        sr,sc = 0, 0
        for _, tr, tc in trees:
            steps = bfs(sr,sc,tr,tc)
            if steps == -1:
                return -1
            else:
                ans+=steps
            sr, sc = tr, tc
        return ans