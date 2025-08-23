# 91 decode ways
# Example 1:
# Input: s = "12"
# Output: 2
# Explanation:
# "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
# Input: s = "226"
# Output: 3
# Explanation:
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
# Input: s = "06"
# Output: 0
# Explanation:
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

class Solution:
    def numDecodings(self, s: str) -> int:
        prev,curr=0,1
        for i in range(len(s)):
            count=0
            if s[i] != '0':
                count = curr
            if i > 0 and s[i - 1] != '0' and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] < '7')):
                count += prev
            prev, curr = curr, count
        return curr

s=Solution()
print(s.numDecodings('12'))
print(s.numDecodings('226'))
print(s.numDecodings('06'))
