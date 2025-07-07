# 122. Best Time to Buy and Sell Stock II
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
#
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
#
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
from itertools import pairwise
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for buy_price, sell_price in pairwise(prices):
            profit = max(0, sell_price - buy_price)
            total_profit += profit

        return total_profit
    # optimised code
    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0,len(prices)-1):
            if prices[i+1]>=prices[i]:
                profit += prices[i+1]-prices[i]
        return profit

s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))