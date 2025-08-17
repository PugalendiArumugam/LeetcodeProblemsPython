# 90 Subsets II
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
from typing import List
class Solution:
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(index, path):
            if index==len(nums):
                result.append(path[:])
                return

            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()

            #skip the duplicate values / the edge case    // this is not really working for the case [4,4,4,1,4] because not in sorted order
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index+=1

            backtrack(index+1,path)

        backtrack(0,[])
        return result
# works
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def depth_first_search(start_index, current_subset):
            result.append(current_subset[:])
            for index in range(start_index, len(nums)):
                if index != start_index and nums[index] == nums[index - 1]:
                    continue
                current_subset.append(nums[index])
                depth_first_search(index + 1, current_subset)
                current_subset.pop()

        result = []
        nums.sort()
        depth_first_search(0, [])
        return result

# this really works well
    def subsetsWithDup3(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res,sol=[],[]
        def backtrack(i):
            if i==n:
                res.append(tuple(sol[:]))
                return
            #dont pick
            backtrack(i+1)
            #pick
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        unq = set(res)
        return list(map(list,unq))



s=Solution()
print(s.subsetsWithDup([1,2,2,3]))
print(s.subsetsWithDup([1,2,2]))
print(s.subsetsWithDup([4,4,4,1,4]))
print(s.subsetsWithDup([0]))
