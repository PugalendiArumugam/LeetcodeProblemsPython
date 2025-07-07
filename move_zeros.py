# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input: nums = [0]
# Output: [0]
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end_zero = 0
        for current, value in enumerate(nums):
            if value != 0:
                nums[end_zero], nums[current] = nums[current], nums[end_zero]
                end_zero += 1
        print(nums)

s=Solution()
s.moveZeroes([0,1,0,3,12])
s.moveZeroes([0])