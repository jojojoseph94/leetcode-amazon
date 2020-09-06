"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

Solution : 
1. Visit all vertices from nodes each one by one - BFS
2. Topological sort
"""

from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Topological sort
        graph = {}
        indegree = {}
        for prereq in prerequisites:
            graph[prereq[0]] = graph.get(prereq[0], []) + [prereq[1]]
            indegree[prereq[1]] = indegree.get(prereq[1], 0) + 1
            indegree[prereq[0]] = indegree.get(prereq[0], 0)
        queue = collections.deque()
        count = len(indegree.keys())
        zero_nodes = 0
        for node, degree in indegree.items():
            if degree == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            zero_nodes+=1
            if node in graph:
                for v in graph[node]:
                    indegree[v]-=1
                    if indegree[v] == 0:
                        queue.append(v)
        return count == zero_nodes

    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def isCycle(vertex, graph, path):
            #if this vertex was visited before
            #from the same starting vertex
            if path[vertex]:
                return True
            path[vertex] = True
            ret = False
            if vertex in graph:
                for v in graph[vertex]:
                    ret = isCycle(v, graph, path)
                    if ret:
                        break
            #backtrack
            path[vertex] = False
            return ret
        graph = {}
        for prereq in prerequisites:
            graph[prereq[0]] = graph.get(prereq[0], []) + [prereq[1]]
        path = [False]*numCourses
        for vertex in graph:
            if isCycle(vertex, graph, path):
                return False
        return True