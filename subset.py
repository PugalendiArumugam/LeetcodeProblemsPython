# 78  Subsets
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(index, path):
            if index==len(nums):
                result.append(path[:])
                return

            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()


            backtrack(index+1,path)

        backtrack(0,[])
        return result

s=Solution()
print(s.subsets([1,2,3]))
print(s.subsets([0]))