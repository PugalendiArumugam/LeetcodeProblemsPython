from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            grid[row][col] = '0'
            for i, j in zip(directions[:-1], directions[1:]):
                new_row, new_col = row + i, col + j
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)

        island_count = 0
        directions = (-1, 0, 1, 0, -1)
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    island_count += 1
        return island_count


s=Solution()
print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

