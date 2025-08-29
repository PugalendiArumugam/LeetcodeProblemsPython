# 282
# Example 1:
# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
#
# Example 2:
# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
#
# Example 3:
# Input: num = "3456237490", target = 9191
# Output: []
# Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def dfs(idx, prev_operand, current_val, expression):
            if idx == len(num):
                if current_val == target:
                    res.append(expression)
                return

            for i in range(idx, len(num)):
                if i != idx and num[idx] == '0':
                    break
                current_operand = int(num[idx: i + 1])
                if idx == 0:
                    dfs(i + 1, current_operand, current_operand, str(current_operand))
                else:
                    dfs(i + 1, current_operand, current_val + current_operand, expression + "+" + str(current_operand))
                    dfs(i + 1, -current_operand, current_val - current_operand, expression + "-" + str(current_operand))
                    dfs(
                        i + 1,
                        prev_operand * current_operand,
                        current_val - prev_operand + (prev_operand * current_operand),
                        expression + "*" + str(current_operand)
                    )
        dfs(0, 0, 0, "")
        return res

s=Solution()
print(s.addOperators("123",6))
print(s.addOperators("232",8))
print(s.addOperators("3456237490",9191))