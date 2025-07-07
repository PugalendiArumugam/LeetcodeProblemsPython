# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# 60. Permutation Sequence
# ==========================
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
#
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"
#
# Example 3:
# Input: n = 3, k = 1
# Output: "123"
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation=[]
        visited=[False]*(n+1)
        for i in range(n):
            factorial=1
            for j in range (1,n-i):
                factorial*=j
            for j in range(1,n+1):
                if not visited[j]:
                    if k>factorial:
                        k -= factorial
                    else:
                        permutation.append(str(j))
                        visited[j]=True
                        break
        return ''.join(permutation)

s=Solution()
# print(s.getPermutation(3,3))
print(s.getPermutation(4,9))
print(s.getPermutation(3,1))

