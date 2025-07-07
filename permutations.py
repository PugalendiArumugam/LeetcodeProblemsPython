from typing import List
# 46. Permutations
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index):
            if index == len_nums:
                result.append(curr[:])
                return
            
            for j in range(len_nums):
                if not visited[j]:
                    visited[j]=True
                    curr[index]=nums[j]
                    backtrack(index+1)
                    visited[j]=False        

        len_nums = len(nums)
        visited = [False] * len_nums
        curr = [0] * len_nums
        result = []
        backtrack(0)
        return result
    
    # Fastest algorithm 
    def permute(self,nums:List[int]) -> List[List[int]]:
        result = []
        def backtrace(path):
            if len(nums) == len(path):
                result.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrace(path)
                path.pop()

        backtrace([])
        return result    

if __name__ == "__main__":
    s = Solution()
    result = s.permute([1,2,3])
    print("Result",result)
    # result = s.permute([0,1])
    # print("Result",result)
    # result = s.permute([1])
    # print("Result",result)
    # result = s.permute([4,5,6,7])
    # print("Result",result)

