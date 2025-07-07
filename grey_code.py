# 89 Gray Code
#
# Example 1:
# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit
#
# Example 2:
# Input: n = 1
# Output: [0,1]
#
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray_codes=[]
        total_numbers = 1 << n
        for i in range(total_numbers):
            gray_number = i ^ (i>>1)
            gray_codes.append(gray_number)
        return gray_codes

    # Simple solution
    def grayCode2(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]

    # Optimized code.  Faster than the first one
    def grayCode3(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        res = [0, 1]
        curr = 2
        for _ in range(2, n + 1):
            curResLen = len(res)
            for i in range(curResLen - 1, -1, -1):
                res.append(res[i] + curr)
            curr *= 2
        return res


s=Solution()
print(s.grayCode(2))
print(s.grayCode2(1))
print(s.grayCode3(4))
