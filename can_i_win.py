# 464 Can I Win?
# In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.
#
# Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.
# Example 1:
# Input: maxChoosableInteger = 10, desiredTotal = 11
# Output: false
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.
#
# Example 2:
# Input: maxChoosableInteger = 10, desiredTotal = 0
# Output: true
#
# Example 3:
# Input: maxChoosableInteger = 10, desiredTotal = 1
# Output: true
from functools import lru_cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(maxsize=None)
        def can_win_game(state: int, current_total: int) -> bool:
            for integer in range(1, maxChoosableInteger + 1):
                if (state >> integer) & 1:
                    continue
                if current_total + integer >= desiredTotal or not can_win_game(state | (1 << integer), current_total + integer):
                    return True
            return False

        sum_of_integers = (1 + maxChoosableInteger) * maxChoosableInteger // 2

        if sum_of_integers < desiredTotal:
            return False

        return can_win_game(0, 0)

    # Optimized logic
    def canIWin2(self, max_c: int, total: int) -> bool:
        if max_c * (max_c + 1) // 2 < total:
            return False
        memo = [-1] * (1 << max_c)

        def solve(can_choose, remain):
            if memo[can_choose] < 0:
                winner = 1
                mask = can_choose
                while mask & -mask:
                    pos = mask & -mask
                    mask ^= pos
                    num = pos.bit_length()
                    if num >= remain or solve(can_choose ^ pos, remain - num) == 1:
                        winner = 0
                        break
                memo[can_choose] = winner
            return memo[can_choose]

        return solve((1 << max_c) - 1, total) == 0

s = Solution()
max_choosable_integer = 20
desired_total = 102
result = s.canIWin(max_choosable_integer, desired_total)
print("Can I win?", result)
