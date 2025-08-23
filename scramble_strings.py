# Example 1:
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: One possible scenario applied on s1 is:
# "great" --> "gr/eat" // divide at random index.
# "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
# "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
# "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
# "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
# "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
# The algorithm stops now, and the result string is "rgeat" which is s2.
# As one possible scenario led s1 to be scrambled to s2, we return true.
#
# Example 2:
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
#
# Example 3:
# Input: s1 = "a", s2 = "a"
# Output: true

from functools import lru_cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def recurse(i: int, j: int, length: int) -> bool:
            if length == 1:
                return s1[i] == s2[j]
            for split in range(1, length):
                if (recurse(i, j, split) and
                        recurse(i + split, j + split, length - split)):
                    return True
                if (recurse(i + split, j, length - split) and
                        recurse(i, j + length - split, split)):
                    return True
            return False

        return recurse(0, 0, len(s1))
    
    #best solution
    map = {}
    def isScramble2(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == s2:
            return True
        a, b, c = [0] * 26, [0] * 26, [0] * 26
        if (s1 + s2) in self.map:
            return self.map[s1 + s2]
        for i in range(1, n):
            j = n - i
            a[ord(s1[i - 1]) - ord('a')] += 1
            b[ord(s2[i - 1]) - ord('a')] += 1
            c[ord(s2[j]) - ord('a')] += 1
            if a == b and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.map[s1 + s2] = True
                return True
            if a == c and self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
                self.map[s1 + s2] = True
                return True
        self.map[s1 + s2] = False
        return False

s=Solution()
print(s.isScramble("great","rgeat"))
print(s.isScramble("abcde", "caebd"))
print(s.isScramble('a','a'))