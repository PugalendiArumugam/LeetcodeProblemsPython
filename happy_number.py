# 202 Happy number
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
# Example 2:
# Input: n = 2
# Output: false
class Solution:
    def isHappy(self, n: int) -> bool:
        # Define a helper function to compute the next number in the sequence
        def get_next_number(x):
            total_sum = 0
            # Continue until x is reduced to zero
            while x:
                # Divide x by 10, saving the remainder and the quotient
                x, digit = divmod(x, 10)
                # Add the square of the remainder to total_sum
                total_sum += digit * digit
            return total_sum

        # Initialize two pointers for detecting cycles (Floyd's cycle detection algorithm)
        slow = n
        fast = get_next_number(n)

        # Loop until the two pointers meet or we find a happy number
        while slow != fast:
            # The slow pointer moves one step at a time
            slow = get_next_number(slow)
            # The fast pointer moves two steps at a time
            fast = get_next_number(get_next_number(fast))

        # The number is happy if and only if the loop ends with slow equals to 1
        return slow == 1

s=Solution()
print(s.isHappy(19))
print(s.isHappy(25))
