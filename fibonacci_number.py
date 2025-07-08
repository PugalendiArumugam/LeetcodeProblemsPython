# 509 Fibonacci number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:
    def fib2(self, n: int) -> int:
        prev, curr= 0,1
        for _ in range(n):
            prev, curr = curr, prev+curr

        return prev

    def fib(self, n:int)->int :
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


s=Solution()
print(s.fib(2))
print(s.fib(8))
print(s.fib(4))
# print(s.fib(64))
