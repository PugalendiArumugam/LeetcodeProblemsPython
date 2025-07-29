# Single Number II  - 137
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Example 1:
# Input: nums = [2, 2, 3, 2]
# Output: 3
#
# Example 2:
# Input: nums = [0, 1, 0, 1, 0, 1, 99]
# Output: 99
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one_number = 0
        more_than_one = 0
        for num in nums:
            current_once = (~one_number & more_than_one & num) | (one_number & ~more_than_one & ~num)
            current_more_than_once = ~one_number & (more_than_one ^ num)
            one_number, more_than_one = current_once, current_more_than_once
        return more_than_one

    def singleNumber2(self, nums: list[int]) -> int:
        # `once` tracks bits that have appeared once
        # `twice` tracks bits that have appeared twice
        once = twice = 0

        for num in nums:
            # Update `once` and `twice` with current number `num`
            # `once` should only hold bits that are exactly seen once so far
            # And `twice` should only hold bits that are exactly seen twice so far
            # Bits seen three times should be cleared from both `once` and `twice`

            # First, calculate `once` considering the current number `num`
            # Use `twice` to mask bits that are already seen two times before
            # because we want to ignore the third time

            # The operations can be explained as:
            # If `once` is already set, and current bit of num is 0, keep `once`
            # If `once` is not set, and `twice` and current bit is set, set `once`
            # This updates bit in `once` only if bit in `num` is 1 and wasn't part
            # of `twice`, or if bit in `num` is 0 and bit was already set in `once`.
            once_new = (~once & twice & num) | (once & ~twice & ~num)

            # Next, calculate `twice` considering the current number `num`
            # Bits in `once` are used to clear bits that appear for the third time
            # This updates bits in `twice` only if bit in `num` is different from bit in `twice`
            # and bit in `once` is 0, to ensure it's not the third time we see this bit.
            twice_new = ~once & (twice ^ num)

            # Update `once` and `twice`
            once, twice = once_new, twice_new

        # Return the number that appears only once
        # All bits in `once` have now appeared either 0 or 3 times, which will end up with 0
        # All bits in `twice` have now appeared exactly once or twice, which end up with 0
        # Only the single number will set bits in `twice`
        return twice

s=Solution()
print(s.singleNumber([2,2,3,2]))
print(s.singleNumber([0,1,0,1,0,1,99]))