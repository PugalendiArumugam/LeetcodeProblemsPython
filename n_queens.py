from typing import List
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                solution.append([''.join(row_state) for row_state in board])
                return
            
            for col in range(n):
                if column[col] + diagonal[row + col] + anti_diagonal[n - row + col] == 0:
                    board[row][col] = "Q"
                    column[col] = diagonal[row + col] = anti_diagonal[n - row + col] = 1
                    backtrack(row + 1)
                    column[col] = diagonal[row + col] = anti_diagonal[n - row + col] = 0
                    board[row][col] = "."
        solution = []
        if n>9 : return solution
        board = [["."] * n for _ in range(n)]
        column = [0] * n
        diagonal = [0] * (2 * n)
        anti_diagonal = [0] * (2 * n)
        backtrack(0)
        return solution

if __name__=="__main__":
    s=Solution()
#    print(s.solveNQueens(4))
    print('*'*25)
#    print(s.solveNQueens(1))
    print('*'*25)
    print(s.solveNQueens(4))