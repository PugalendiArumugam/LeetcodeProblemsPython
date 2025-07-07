from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = max_window = nums[0]

        for num in nums[1:]:
            if curr < 0:
                curr = num
            else:
                curr += num
            if curr > max_window:
                max_window = curr
        return max_window
    
        # login usex max function ... not optimized
        # =========================================
        # max_sum = current_sum = nums[0]      
        # for num in nums[1:]:
        #     current_sum = max(current_sum + num, num)
        #     max_sum = max(max_sum, current_sum)
        # return max_sum


    def maxSubArray2(self, nums: List[int]) -> int:
        sum_window = max_window = nums[0]

        for num in nums[1:]:
            if sum_window < 0:
                sum_window = num
            else:
                sum_window += num
            if sum_window > max_window:
                max_window = sum_window
        return max_window
    
# if __name__=="__main__":  
s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5,4,-1,7,8]))
