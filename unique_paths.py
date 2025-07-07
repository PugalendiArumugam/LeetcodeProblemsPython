# 62. Unique Paths
# Example 1:
# Input: m = 3, n = 7
# Output: 28
#
# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [1] * n
        for row in range(1, m):
            for col in range(1, n):
                result[col] += result[col - 1]

        return result[-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        # Initialize a list that will hold the number of unique paths to each cell
        # in the first row. Initially, there's only one unique path to reach any cell
        # in the first row since the only possible move is to the right.
        path_counts = [1] * n

        # Iterate over the rows of the grid starting from the second row,
        # since the first row has been initialized already.
        for row in range(1, m):
            # Iterate over the columns starting from the second column,
            # since the first column only has one unique path (move down).
            for col in range(1, n):
                # The number of unique paths to reach this cell is the sum of
                # the number of unique paths to reach the cell directly above
                # and the number of unique paths to reach the cell to the left.
                path_counts[col] += path_counts[col - 1]

        # Return the number of unique paths to reach the bottom-right corner of the grid,
        # which is the last element in the path_counts list.
        return path_counts[-1]

s=Solution()
print(s.uniquePaths(3,8))
print(s.uniquePaths(3,2))
