# 154. Find Minimum in Rotated Sorted Array II
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
# You must decrease the overall operation steps as much as possible.
#
# Example 1:
# Input: nums = [1,3,5]
# Output: 1
#
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[r]:    # smallest element must be at the right of mid
                l=mid+1
            elif nums[mid] < nums[r] : # smallest element must be at the left of mid
                r=mid
            else:
                r-=1     # move the right pointer left
        return nums[l]

s=Solution()
print(s.findMin([1,3,5]))
print(s.findMin([2,2,2,0,1]))