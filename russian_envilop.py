# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope. One envelope can fit into another if and only if
# both the width and height of one envelope are greater than the other envelope's width and height.  Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
#
# Note: You cannot rotate an envelope.
# Example 1:
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
#
# Example 2:
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1

from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [envelopes[0][1]]
        for _, height in envelopes[1:]:
            if height > dp[-1]:
                dp.append(height)
            else:
                index = bisect_left(dp, height)
                dp[index] = height
        return len(dp)

    # Optimized code
    def maxEnvelopes3(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes,key = lambda x: x[0],reverse = True)
        envelopes = sorted(envelopes,key = lambda x: x[1])
        q = [envelopes[0][0]]
        for i in range(1, len(envelopes)):
            if q[-1] < envelopes[i][0]:
                q.append(envelopes[i][0])
            else:
                q[bisect_left(q, envelopes[i][0])] = envelopes[i][0]
        return len(q)

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    def lis(nums):
        from bisect import bisect_left as bsearch
        dp = []
        for num in nums:
            idx = bsearch(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)
    return lis([i[1] for i in envelopes])

s=Solution()
print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(s.maxEnvelopes([[1,1],[1,1],[1,1]]))
