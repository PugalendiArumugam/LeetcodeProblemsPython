# 79 Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
from typing import List, Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        W=len(word)

        if m==1 and n==1:
            return board[0][0]==word

        def backtrack(pos, index):
            i,j=pos

            if index==W:
                return True

            if board[i][j]!=word[index]:
                return False

            save_char=board[i][j]
            board[i][j]='#'

            for i_offset, j_offset in [(0,1),(1,0),(0,-1),(-1,0)]:
                row, col= i+i_offset, j+j_offset
                if 0 <= row < m and 0 <= col < n:
                   if backtrack((row,col),index+1):
                      return True

            board[i][j]=save_char
            return False

        for i in range(m):
            for j in range(n):
                if backtrack((i,j),0):
                    return True

        return False

    def exist2(self, board: List[List[str]], word: str) -> bool:

        R = len(board)
        C = len(board[0])

        if len(word) > R * C:
            return False

        count = Counter(sum(board, []))

        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C or word[i] != board[r][c] or (r, c) in seen:
                return False

            seen.add((r, c))
            res = (
                    dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1)
            )
            seen.remove((r, c))  # backtracking

            return res

        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True
        return False

s=Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))

