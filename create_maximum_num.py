from typing import List

# 321 Create maximum number
# You are given two integer arrays nums1 and nums2 of lengths m and n respectively.nums1 and nums2 represent the digits of two numbers.You are also given an integer k.
# Create the maximum number of length k <= m + n from digits of the two numbers.The relative order of the digits from the same array must be preserved.
# Return an array of the k digits representing the answer.
#
# Example 1:
# Input: nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5
# Output: [9, 8, 6, 5, 3]
#
# Example 2:
# Input: nums1 = [6, 7], nums2 = [6, 0, 4], k = 5
# Output: [6, 7, 6, 0, 4]
#
# Example 3:
# Input: nums1 = [3, 9], nums2 = [8, 9], k = 3
# Output: [9, 8, 9]

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def find_max_sequence(nums: List[int], k: int) -> List[int]:
            stack = [0] * k
            to_remove = len(nums) - k
            top = -1

            for num in nums:
                while top >= 0 and stack[top] < num and to_remove > 0:
                    top -= 1
                    to_remove -= 1
                if top + 1 < k:
                    top += 1
                    stack[top] = num
                else:
                    to_remove -= 1

            return stack

        def is_greater(nums1: List[int], nums2: List[int], i: int, j: int) -> bool:
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                i += 1
                j += 1
            return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])

        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            merged = []
            i = j = 0
            while i < len(nums1) or j < len(nums2):
                if is_greater(nums1, nums2, i, j):
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            return merged

        best_sequence = [0] * k
        for count in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            candidate1 = find_max_sequence(nums1, count)
            candidate2 = find_max_sequence(nums2, k - count)
            candidate_merged = merge(candidate1, candidate2)
            if best_sequence < candidate_merged:
                best_sequence = candidate_merged

        return best_sequence

s=Solution()
print(s.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5))