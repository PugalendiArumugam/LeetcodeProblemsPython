# 315. Count of Smaller Numbers After Self
# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
#
# Example 1:
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
# Example 2:
# Input: nums = [-1]
# Output: [0]
#
# Example 3:
# Input: nums = [-1,-1]
# Output: [0,0]
from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        smaller_arr = [0] * len(nums)

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            l, r = 0, 0
            while l < len(left) or r < len(right):
                if r >= len(right) or (l < len(left) and left[l][1] <= right[r][1]):
                    result.append(left[l])
                    smaller_arr[left[l][0]] += r
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            return result

        merge_sort(list(enumerate(nums)))
        return smaller_arr

    #optimized code
    def countSmaller2(self, nums: List[int]) -> List[int]:
        offset = min(nums) - 1
        N = max(nums)-offset
        bit = [0] * (N+1)
        res = []

        for num in reversed(nums):
            ind = num-offset-1
            cnt = 0
            while ind:
                cnt += bit[ind]
                ind -= ind & -ind

            res.append(cnt)

            ind = num-offset
            while ind <= N:
                bit[ind] += 1
                ind += ind & -ind

        return res[::-1]

s=Solution()
res = s.countSmaller2([5,2,6,1])
print(" ".join(map(str, res)))
res = s.countSmaller([-1])
print(" ".join(map(str, res)))
res = s.countSmaller([-1,-1])
print(" ".join(map(str, res)))
