# 389
# Example 1:
#
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:
#
# Input: s = "", t = "y"
# Output: "y"

from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = Counter(s)
        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return char

    def findTheDifference2(self, s: str, t: str) -> str:
        result=0
        for i in s+t:
            result^=ord(i)
        return chr(result)

s=Solution()
print(s.findTheDifference("abcd","abcde"))
print(s.findTheDifference("","ab"))
print(s.findTheDifference("ab","abcde"))
print(s.findTheDifference("abcd","abcd"))
