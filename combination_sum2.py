# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: [
# [1,2,2],
# [5]
# ]
from typing import List

class Solution():
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start: int, curr_sum:int):
            if curr_sum == 0:
                all_combinations.append(combination[:])
                return
            if start>=len(candidates) or curr_sum<candidates[start]:
                return

            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                combination.append(candidates[i])
                dfs(i+1,curr_sum-candidates[i])
                combination.pop()

        candidates.sort();
        combination=[]
        all_combinations=[]
        dfs(0,target)
        return all_combinations

s=Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))
print(s.combinationSum2([2,5,2,1,2],5))
