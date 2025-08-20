# 456 132 pattern - monotonic
# Example 1:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
#
# Example 2:
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#
# Example 3:
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        x_value = float('-inf')
        stack = []
        for number in reversed(nums):
            if number <  x_value:
                return True
            while stack and stack[-1] < number:
                x_value = stack.pop()
            stack.append(number)
        return False

s=Solution()
print(s.find132pattern([1,2,3,4]))
print(s.find132pattern([3,1,4,2]))
print(s.find132pattern([-1,3,2,0]))