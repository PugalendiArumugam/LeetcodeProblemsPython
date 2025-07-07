# 165. Compare Version Numbers
# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
#
# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.
#
# Return the following:
#
# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.
# Example 1:
# Input: version1 = "1.2", version2 = "1.10"
# Output: -1
# Explanation:
# version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.
#
# Example 2:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation:
# Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
#
# Example 3:
# Input: version1 = "1.0", version2 = "1.0.0.0"
# Output: 0
# Explanation:
# version1 has less revisions, which means every missing revision are treated as "0".
class Solution:
    def compareVersion2(self, version1: str, version2: str) -> int:
        len1, len2 = len(version1), len(version2)
        p1 = p2 = 0
        while p1 < len1 or p2 < len2:
            num1 = num2 = 0
            while p1 < len1 and version1[p1] != '.':
                num1 = num1 * 10 + int(version1[p1])
                p1 += 1
            while p2 < len2 and version2[p2] != '.':
                num2 = num2 * 10 + int(version2[p2])
                p2 += 1
            if num1 != num2:
                return -1 if num1 < num2 else 1

            p1, p2 = p1 + 1, p2 + 1
        return 0

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        max_len = max(len(v1), len(v2))
        for i in range(max_len):
            num1 = v1[i] if i < len(v1) else 0
            num2 = v2[i] if i < len(v2) else 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0

s=Solution()
print(s.compareVersion("1.2","1.10"))
print(s.compareVersion("1.01","1.001"))
print(s.compareVersion("1.0","1.0.0.0"))
print(s.compareVersion("1.01.1","1.1.1"))