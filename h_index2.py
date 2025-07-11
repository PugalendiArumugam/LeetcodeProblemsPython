# 275. H-Index II
# Example 1:
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
#
# Example 2:
# Input: citations = [1,2,100]
# Output: 2
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citation_length = len(citations)
        left, right = 0, citation_length
        while left < right:
            mid = (left + right + 1) // 2
            if citations[citation_length - mid] >= mid:
                left = mid
            else:
                right = mid - 1
        return left

s=Solution()
print(s.hIndex([0,1,3,5,6]))
print(s.hIndex([1,2,100]))
