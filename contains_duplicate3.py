# 220 contains duplicate III
# You are given an integer array nums and two integers indexDiff and valueDiff.
# Find a pair of indices (i, j) such that:
# a) i != j,
# b) abs(i - j) <= indexDiff.
# c) abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.
from typing import List
from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sorted_set = SortedSet()
        for i, num in enumerate(nums):
            l_idx = sorted_set.bisect_left(num - valueDiff)
            if l_idx < len(sorted_set) and sorted_set[l_idx] <= num + valueDiff:
                return True
            sorted_set.add(num)
            if i >= indexDiff:
                sorted_set.remove(nums[i - indexDiff])
        return False

    # optimized code
    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(set(nums)) == len(nums): return False
        bucket = {}
        width = t + 1
        for i, n in enumerate(nums):
            bucket_i = n // width
            if bucket_i in bucket:
                return True
            elif bucket_i + 1 in bucket and abs(n - bucket[bucket_i + 1]) < width:
                return True
            elif bucket_i - 1 in bucket and abs(n - bucket[bucket_i - 1]) < width:
                return True

            bucket[bucket_i] = n
            if i >= k: del bucket[nums[i - k] // width]
        return False

s=Solution()
print(s.containsNearbyAlmostDuplicate([1,2,3,1],3,0))
print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))