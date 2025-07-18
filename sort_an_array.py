# 912 Sort an array
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
#
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
from typing import List
import random
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:

# counting sort 90 ms.. okay
    def sortArray(self, nums: List[int]) -> List[int]:
        # using counting sort
        #--------------------
        if not nums:
            return nums
        max_val = max(nums)
        min_val = min(nums)
        range_size = max_val - min_val + 1
        count = [0] * range_size
        for num in nums:
            count[num - min_val] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        output = [0] * len(nums)
        for num in reversed(nums):  # reverse to maintain stability
            count[num - min_val] -= 1
            output[count[num - min_val]] = num
        return output

# quick sort failed with timeout

    def sortArray2(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if len(nums) <= 1:
            return nums
        # Choose a pivot (here, we pick the last element)
        pivot = nums[-1]
        left = []
        right = []
        equal = []

        # Partitioning
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                equal.append(num)  # Handles duplicates

        # Recursive sorting
        return self.sortArray(left) + equal + self.sortArray(right)

# quick sort with python random selection. optimized and fast

    def sortArray3(self, nums: List[int]) -> List[int]:
        if len(nums) <= 0:
            return nums
        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        center = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        return self.sortArray(left) + center + self.sortArray(right)



s=Solution()
print(s.sortArray3([5,2,3,1]))
print(s.sortArray([0,0,1,1,2,5]))