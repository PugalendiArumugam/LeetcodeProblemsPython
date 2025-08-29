# 479
# Example 1:
# Input: n = 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
# Example 2:
# Input: n = 1
# Output: 9

class Solution:
    def largestPalindrome(self, n: int) -> int:
        max_num = 10**n - 1
        for first_half in range(max_num, max_num // 10, -1):
            reversed_half = first_half
            palindrome = first_half
            while reversed_half:
                palindrome = palindrome * 10 + reversed_half % 10
                reversed_half //= 10

            factor = max_num
            while factor * factor >= palindrome:
                if palindrome % factor == 0:
                    return palindrome % 1337
                factor -= 1
        return 9
    # simplest solution
    def largestPalindrome2(self, n: int) -> int:
        return [0, 9, 987, 123, 597, 677, 1218, 877, 475][n]

s=Solution()
print(s.largestPalindrome(2))
print(s.largestPalindrome(1))
print(s.largestPalindrome(4))
print(s.largestPalindrome(5))
print(s.largestPalindrome(8))
