# 80 remove duplicates form sorted array ii
# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=0
        for num in nums:
            if counter<2 or num !=nums[counter-2]:
                nums[counter]=num
                counter+=1
        return counter

    #best solution
    def removeDuplicates1(self, nums: List[int]) -> int:
        double = False
        left = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                double = False
                nums[left]=nums[i]
                left+=1
            else:
                if not double:
                    double=True
                    nums[left]=nums[i]
                    left+=1
        return left

s=Solution()
print(s.removeDuplicates([1]))
print(s.removeDuplicates([1,1,1,2,2,3]))
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))


