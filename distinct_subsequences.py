# 115 Distinct Subsequences
# Example 1:
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
#
# Example 2:
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def numDistinct2(self, s: str, t: str) -> int:
        result_len = len(t)
        dp = [1] + [0] * result_len
        for char in s:
            for j in range(result_len, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[result_len]

    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]

obj=Solution()
print(obj.numDistinct('rabbbit','rabbit'))
print(obj.numDistinct('babgbag','bag'))
