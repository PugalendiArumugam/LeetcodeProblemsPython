#150
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
from collections import deque
from typing import List, Deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result=[]
        for token in tokens:
            if token.isdigit() or len(token) > 1 :
                result.append(int(token))
            else:
                if token == "+":
                    result[-2] += result[-1]
                elif token == "-":
                    result[-2] -= result[-1]
                elif token == "*":
                    result[-2] *= result[-1]
                else: # assume division
                    result[-2] = int(float(result[-2]) / result[-1])
                result.pop()

        return result[0]

    #optimised code
    def evalRPN2(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = deque([])
        for i in tokens:
            if i not in {'+','-','*','/'}:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    ans = b+a
                if i == '-':
                    ans = b-a
                if i == '*':
                    ans = b*a
                if i == '/':
                    ans = int(b/a)
                stack.append(ans)
        return stack.pop()

s=Solution()
# print(s.evalRPN2(["2","1","+","3","*"]))
# print(s.evalRPN2(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
