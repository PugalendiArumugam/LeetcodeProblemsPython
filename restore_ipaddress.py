# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#
# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]
#
# Example 3:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
from typing import List
class Solution:
    def restoreIpAddresses1(self, s: str) -> List[str]:
        def is_valid(s, start, end):
            if start > end:
                return False
            if s[start] == '0' and start != end:
                return False
            num = int(s[start:end+1])
            return 0 <= num <= 255

        def backtracking(index, path):
            if index == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return

            if len(path) > 4:
                return

            for i in range(index, min(index + 3, len(s))):
                if is_valid(s, index, i):
                    sub = s[index:i+1]
                    path.append(sub)
                    backtracking(i+1, path)
                    path.pop()
        res = []
        backtracking(0, [])
        return res

s=Solution()
print(s.restoreIpAddresses1("25525511135"))
print(s.restoreIpAddresses1("0000"))
print(s.restoreIpAddresses1("101023"))