# 131
# ===
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#
# Example 2:
# Input: s = "a"
# Output: [["a"]]


#DFS and DP
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(start_index: int):
            if start_index == length:
                result.append(curr[:])
                return

            for end_index in range(start_index, length):
                if palindrome_ok[start_index][end_index]:
                    curr.append(s[start_index:end_index + 1])
                    dfs(end_index + 1)
                    curr.pop()

        length = len(s)

        palindrome_ok = [[True] * length for _ in range(length)]

        for i in reversed(range(length)):
            for j in range(i + 1, length):
                palindrome_ok[i][j] = s[i] == s[j] and palindrome_ok[i + 1][j - 1]

        result = []
        curr = []
        dfs(0)
        return result

so=Solution()
print(so.partition("aab"))
print(so.partition("abab"))
print(so.partition("abaabaa"))
print(so.partition("a"))
