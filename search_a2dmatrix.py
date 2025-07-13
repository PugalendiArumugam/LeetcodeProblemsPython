# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row,n_col=len(matrix),len(matrix[0])
        l,r=0,n_row*n_col-1
        while l<r:
            mid=(l+r) >> 1
            row,col = divmod(mid,n_col)     # mid convert to row col.  (2D)
            if matrix[row][col] >= target:   # mid is greater than equal to target go to left
                r=mid
            else:
                l=mid+1
        return matrix[l//n_col][l%n_col] == target
s=Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))


