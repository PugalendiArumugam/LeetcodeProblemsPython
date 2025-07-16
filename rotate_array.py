# 189 - Rotate array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # l=(len(nums)-k)    # this is wrong.. if 10 then rotation should be 3
        # nums[:] = nums[-k:]+nums[:l]
        # print(nums)

        k %= len(nums) # if 5 then k= 5%7=5, if 10 then 10%7 = 3 which is correct rotation
        # The last k elements are moved to the front and the remainder are appended
        nums[:] = nums[-k:] + nums[:-k]
        print(nums[-k:])   # from -k which from -3
        print(nums[:-k])   # upto -k which upto -3
        print(nums)

        # arr = [1, 2, 3, 4, 5, 6, 7]
        # n = 3
        # subarray = arr[-n:]
        # n = len(arr)-n
        # subarray2 = arr[:n]
        # print(subarray,subarray2)

s=Solution()
s.rotate([1,2,3,4,5,6,7],3)
s.rotate([1,2,3,4,5,6,7],5)
s.rotate([1,2,3,4,5,6,7],2)
s.rotate([1,2,3,4,5,6,7],1)
s.rotate([1,2,3,4,5,6,7],0)
s.rotate([1,2,3,4,5,6,7],10)

