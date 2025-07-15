# 47 Permutations II
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int):
            if index == size:
                result.append(curr[:])
                return
            for j in range(size):
                if visited[j] or (j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]):
                    continue
                curr[index] = nums[j]
                visited[j] = True
                backtrack(index + 1)
                visited[j] = False

        size = len(nums)
        nums.sort()
        result = []
        curr = [0] * size
        visited = [False] * size
        backtrack(0)

        return result

s=Solution()
print(s.permuteUnique([1,1,2]))
print(s.permuteUnique([1,2,3]))
