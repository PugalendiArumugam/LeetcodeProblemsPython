# 392 is subsequence
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first_idx=0
        sec_idx=0
        while first_idx < len(s) and sec_idx < len(t):
            if s[first_idx] == t[sec_idx]:
                first_idx += 1

            sec_idx+=1

        return first_idx==len(s)
s=Solution()
print(s.isSubsequence("abc","ahbgdc"))
print(s.isSubsequence("axc","ahbgdc"))
