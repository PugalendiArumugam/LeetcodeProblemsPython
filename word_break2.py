# 140 Word Break II
# -------------------
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
#
# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(start, path):
            if start == len(s):
                ans.append(" ".join(path))
                return
            for end in range(start, len(s)):
                w = s[start:end + 1]
                if w in wordDict:
                    path.append(w)
                    dfs(end + 1, path)
                    path.pop()

        ans = []
        dfs(0, [])
        return ans

s=Solution()
print(s.wordBreak("catsanddog",["cat","cats","and","sand","dog"]))
print(s.wordBreak("pineapplepenapple",["apple","pen","applepen","pine","pineapple"]))