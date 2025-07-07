from typing import List
# 46 - Permutations
# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.


class solution:
    def candy(self, ratings: List[int]) -> int:
        num_children = len(ratings)
        left_calc = [1] * num_children
        right_calc = [1] * num_children
        for i in range(1, num_children):
            if ratings[i] > ratings[i - 1]:
                left_calc[i] = left_calc[i - 1] + 1
      
        for i in range(num_children - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_calc[i] = right_calc[i + 1] + 1
    
        total_candies = sum(max(candies_left, candies_right) for candies_left, candies_right in zip(left_calc, right_calc))      
        return total_candies


if __name__ == "__main__":
    # s = solution()
    # result = s.candy([1, 0, 2])
    result = solution().candy([1, 0, 2])
    print("Result:", result)
    result = solution().candy([1, 2, 2])
    print("Result:", result)
    result = solution().candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0])
    print("Result:", result)
    result = solution().candy([100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60])
    print("Result:", result)
    