from typing import List
# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
#
# Example 2:
# Input: triangle = [[-10]]
# Output: -10

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        num_rows=len(triangle)
        path_sum=[0]* (num_rows + 1)
        for row in range(num_rows - 1, -1, -1):
            for col in range(row + 1):
                path_sum[col] = min(path_sum[col], path_sum[col + 1]) + triangle[row][col]
        return path_sum[0]

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[0]*(n+1)for _ in range(n+1)]
        for i in range(n-1,-1,-1):
          for j in range(i+1):
            dp[i][j]=triangle[i][j]+min((dp[i+1][j]),(dp[i+1][j+1]))
        return dp[0][0]

s=Solution()
print(s.minimumTotal2([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal([[-10]]))
