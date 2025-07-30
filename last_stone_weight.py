# 1046. Last Stone Weight
# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
#
# Example 2:
# Input: stones = [1]
# Output: 1
from heapq import heapify, heappush, heappop
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]      # invert the values
        heapify(h)
        while len(h) > 1:
            stone1 = -heappop(h)
            stone2 = -heappop(h)
            if stone1 != stone2:
                heappush(h, -(stone1 - stone2))
        return 0 if not h else -h[0]

s=Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
print(s.lastStoneWeight([1]))
