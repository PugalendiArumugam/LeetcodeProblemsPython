# 152. Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = current_max = current_min = nums[0]
        for num in nums[1:]:
            temp_max, temp_min = current_max, current_min
            current_max = max(num, temp_max * num, temp_min * num)
            current_min = min(num, temp_max * num, temp_min * num)
            max_product = max(max_product, current_max)
        return max_product

    def maxProduct2(self, nums: List[int]) -> int:
        reverse_nums=nums[::-1]
        for i in range(1,len(nums)):
            nums[i]*=nums[i-1] or 1
            reverse_nums[i]*=reverse_nums[i-1] or 1
        return max(nums+reverse_nums)

s=Solution()
print(s.maxProduct2([2,3,-2,4]))
print(s.maxProduct2([-2,0,-1]))
