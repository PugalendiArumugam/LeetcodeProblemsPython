# 151. Reverse Words in a String
# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
#
# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        r=reversed(words)
        result=' '.join(r)
        return result

s=Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))