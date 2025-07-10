# 414- Third Maximum Number
# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
#
# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
#
# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
from math import inf
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max=sec_max=third_max=-inf
        for num in nums:
            if num in [first_max, sec_max, third_max]:
                continue
            if num > first_max:
                third_max, sec_max, first_max = sec_max, first_max, num
            elif num > sec_max:
                third_max, sec_max = sec_max, num
            elif num > third_max:
                third_max = num
        return third_max if third_max != -inf else first_max

s=Solution()
print(s.thirdMax([3,2,1]))
print(s.thirdMax([1,2]))
print(s.thirdMax([2,2,3,1]))