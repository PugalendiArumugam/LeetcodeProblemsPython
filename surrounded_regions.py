# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#
# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
#
# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
#
# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print("Input",board)
        def depth_first_search(i: int, j: int) -> None:
            board[i][j] = '.'
            vectors = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            for vector in vectors:
                x, y = i + vector[0], j + vector[1]
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'O':
                    depth_first_search(x, y)

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                is_border_cell = i in (0, rows - 1) or j in (0, cols - 1)
                if board[i][j] == 'O' and is_border_cell:
                    depth_first_search(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'
        print("Output",board)
        print()

    def solve6(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'S'  # Mark as safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Mark border-connected 'O's
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # 2. Flip inner 'O' to 'X', and safe 'S' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'



s=Solution()
s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
s.solve([["X"]])

