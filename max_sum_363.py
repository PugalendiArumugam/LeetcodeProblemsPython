# 363. Max Sum of Rectangle No Larger Than K
# Example 1:
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
#
# Example 2:
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
from sortedcontainers import SortedSet
from math import inf
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        r_len, c_len = len(matrix), len(matrix[0])

        infinity_value = -inf       # max value

        for starting_row in range(r_len):
            # A list to store row sums
            row_sums = [0] * c_len

            # Iterate over the ending row of our submatrix
            for ending_row in range(starting_row, r_len):
                # Update the row sums by adding corresponding values from the new row
                for col in range(c_len):
                    row_sums[col] += matrix[ending_row][col]

                # Initialize current sum and create a sorted set to store prefix sums
                current_sum = 0
                sorted_prefix_sums = SortedSet([0])

                # Iterating over the cumulative sum of row elements
                for sum_value in row_sums:
                    current_sum += sum_value
                    # Find the index of the smallest prefix sum so that
                    # current_sum - prefix_sum <= k and we get the biggest current_sum possible
                    index = sorted_prefix_sums.bisect_left(current_sum - k)
                    # If such index exists in the sorted set, update the max_sum
                    if index != len(sorted_prefix_sums):
                        max_sum = max(infinity_value, current_sum - sorted_prefix_sums[index])
                    # Add the current prefix sum to the sorted set
                    sorted_prefix_sums.add(current_sum)

        # Return the maximum sum found that is less than or equal to 'k'
        return infinity_value

s=Solution()
print(s.maxSumSubmatrix([[1,0,1],[0,-2,3]],2))