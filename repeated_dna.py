# 187. Repeated DNA Sequences
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
#
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
#
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
from collections import Counter
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_count = Counter()
        repeated_sequences = []
        num_substrings = len(s) - 10
        for i in range(num_substrings + 1):
            subsequence = s[i: i + 10]
            sequence_count[subsequence] += 1
            if sequence_count[subsequence] == 2:
                repeated_sequences.append(subsequence)
        return repeated_sequences

    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        if len(s) < 10 or len(s) >= 10 ** 5: return []
        seen, duplicates = set(), set()

        for r in range(len(s) - 10 + 1):
            curSeq = s[r:r+10]
            if curSeq in seen:
                duplicates.add(curSeq)
            else: seen.add(curSeq)

        return list(duplicates)

    def findRepeatedDnaSequences4(self, s: str) -> List[str]:
        repeated = set()
        single = set()
        if len(s) < 10 or len(s) >= 10**5:
            return []

        for i in range(len(s)-9):
            if s[i:10+i] not in single:
                single.add(s[i:10+i])
            else :
                repeated.add(s[i:10+i])
        return list(repeated)

s=Solution()
print(s.findRepeatedDnaSequences4("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(s.findRepeatedDnaSequences("AAAAAAAAAAAAA"))