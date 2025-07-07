# 546 Remove boxes
# You are given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes
# with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.
# Return the maximum points you can get.
# Example 1:
# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
#
# Example 2:
# Input: boxes = [1,1,1]
# Output: 9
#
# Example 3:
# Input: boxes = [1]
# Output: 1
from itertools import groupby
from typing import List
from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dfs(start, end, continuous_count):
            if start > end:
                return 0
            while start < end and boxes[end] == boxes[end - 1]:
                end -= 1
                continuous_count += 1

            score = dfs(start, end - 1, 0) + (continuous_count + 1) ** 2

            for middle in range(start, end):
                if boxes[middle] == boxes[end]:
                    score = max(score, dfs(middle + 1, end - 1, 0) + dfs(start, middle, continuous_count + 1))
            return score

        total_score = dfs(0, len(boxes) - 1, 0)

        dfs.cache_clear()

        return total_score

    # Optimised link
    def removeBoxes3(self, boxes: List[int]) -> int:

        boxes = tuple((k, len(list(g))) for k, g in groupby(boxes))

        @lru_cache(None)
        def dfs(grps: tuple) -> int:

            if not grps: return 0
            (colorL, lenL), grps = grps[0], grps[1:]

            res = lenL * lenL + dfs(grps)

            for i, (colorR, lenR) in enumerate(grps):
                if colorL == colorR:
                    res = max(res, dfs(grps[:i]) +
                              dfs(((colorL, lenL + lenR),) + grps[i + 1:]))

            return res

        return dfs(boxes)

s=Solution()
print(s.removeBoxes([1,3,2,2,2,3,4,3,1]))
print(s.removeBoxes([1,2,2,1,2,2,1]))