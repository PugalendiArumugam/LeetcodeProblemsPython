# 162 find peak element
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
#
# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

from typing import List
class Solution:

    # O(n log n) correct one with binary search
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        return l

    # O(n) but not correct .. this is standard template
    def findPeakElement1(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1





s=Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
print(s.findPeakElement([1]))
print(s.findPeakElement([1,3]))
print(s.findPeakElement([2,1,3]))
