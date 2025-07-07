# 3597. Partition String
# Given a string s, partition it into unique segments according to the following procedure:
#
# Start building a segment beginning at index 0.
# Continue extending the current segment character by character until the current segment has not been seen before.
# Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.
# Repeat until you reach the end of s.
# Return an array of strings segments, where segments[i] is the ith segment created
#
# Example 1:
# Input: s = "abbccccd"
# Output: ["a","b","bc","c","cc","d"]
#
# Example 2:
# Input: s = "aaaa"
# Output: ["a","aa"]

from typing import List
class Solution:
    def partitionString(self, s: str) -> List[str]:
        visited = set([])
        result = []
        curr=""
        for char in s:
            curr +=char
            if curr not in visited:
                visited.add(curr)
                result.append(curr)
                curr=""
        return result

    def partitionString2(self, s: str) -> List[str]:
        seen = set()
        segments = []
        current = ""
        for char in s:
            current += char
            if current not in seen:
                seen.add(current)
                segments.append(current)
                current = ""
        return segments

    def partitionString3(self, s: str) -> List[str]:
        # build a set to store the string
        # if string in set, add more char into string and check again
        # i wonderd if it is posible that we can't add the string
        # i mean like input s="aaaa"
        # output="a", "aa" and we just drop the last a

        bucket = set()
        res = []
        prefix = ""

        for char in s:
            prefix += char
            if prefix not in bucket:
                bucket.add(prefix)
                res.append(prefix)
                prefix = ""

        return res

s=Solution()
print(s.partitionString("abbccccd"))
print(s.partitionString("aaaa"))



