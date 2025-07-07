# 63. Unique Paths II
# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        result_dp = [[0] * cols for _ in range(rows)]

        if obstacleGrid[0][0] == 0:
            result_dp[0][0] = 1

        for i in range(1, rows):
            if obstacleGrid[i][0] == 0:
                result_dp[i][0] = result_dp[i - 1][0]

        for j in range(1, cols):
            if obstacleGrid[0][j] == 0:
                result_dp[0][j] = result_dp[0][j - 1]

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    result_dp[i][j] = result_dp[i - 1][j] + result_dp[i][j - 1]

        return result_dp[-1][-1]

s=Solution()
result=s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(result)
result=s.uniquePathsWithObstacles([[0,1],[0,0]])
print(result)