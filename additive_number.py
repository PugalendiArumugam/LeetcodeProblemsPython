# 306
#
# An additive number is a string whose digits can form an additive sequence.
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
# Given a string containing only digits, return true if it is an additive number or false otherwise.
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Example 1:
# Input: "112358"
# Output: true
# Explanation:
# The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
# Example 2:
# Input: "199100199"
# Output: true
# Explanation:
# The additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(first, second, remaining):
            if not remaining:
                return True
            if first + second > 0 and remaining[0] == '0':
                return False
            for i in range(1, len(remaining) + 1):
                if first + second == int(remaining[:i]):
                    if dfs(second, first + second, remaining[i:]):
                        return True
            return False

        n = len(num)
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if i > 1 and num[0] == '0':     # if leading zeros skip
                    break
                if j - i > 1 and num[i] == '0':
                    continue
                if dfs(int(num[:i]), int(num[i:j]), num[j:]):
                    return True
        return False


    def isAdditiveNumber2(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            for j in range(i+1, n):
                if num[i] == '0' and j - i > 1:
                    break
                num1, num2 = num[:i], num[i:j]
                k = j
                while k < n:
                    num3 = str(int(num1) + int(num2))
                    if not num.startswith(num3, k):
                        break
                    k += len(num3)
                    num1, num2 = num2, num3
                if k == n:
                    return True
        return False

s=Solution()
print(s.isAdditiveNumber("112358"))
print(s.isAdditiveNumber2("199100199"))
