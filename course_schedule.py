# Course Schedule - 207
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
from collections import defaultdict, deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        dp = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            dp[course] += 1

        queue = deque([i for i in range(numCourses) if dp[i] == 0])
        result = 0
        while queue:
            course = queue.popleft()
            result += 1
            for successor in graph[course]:
                dp[successor] -= 1
                if dp[successor] == 0:
                    queue.append(successor)

        return result == numCourses

s=Solution()
print(s.canFinish(2,[[1,0]]))
print(s.canFinish(2,[[1,0],[0,1]]))

