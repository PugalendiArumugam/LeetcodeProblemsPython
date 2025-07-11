# 274. H-Index    (this is unsorted - we need to use counting sort technique)
# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
#
# Example 2:
# Input: citations = [1,3,1]
# Output: 1
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        f = [0] * (n + 1)
        for c in citations:
            if c >= n:
                f[n] += 1
            else:
                f[c] += 1
        idx = n
        s = f[n]
        while s < idx:
            idx -= 1
            s += f[idx]
        return idx

s=Solution()
print(s.hIndex([6, 0, 3, 5, 3]))   #3
print(s.hIndex([3,0,6,1,5]))   #3
print(s.hIndex([1,3,1]))  #1
