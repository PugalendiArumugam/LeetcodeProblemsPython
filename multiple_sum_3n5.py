# If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .
# Find the sum of all the multiples of  or  below .

# input
# 2
# 10
# 100

# output
# 23
# 2318

class Solution:  
    def sum_up(self,n)->int:
        n1=sum_val(n,3)
        n2=sum_val(n,5)
        n3=sum_val(n,15)
        return n1+n2-n3

def sum_val(n:int,k:int)->int:
        d = n // k
        return k * (d * (d+1)) // 2

if __name__ == "__main__":
    s = Solution()
    print(s.sum_up(2-1))
    print(s.sum_up(10-1))
    print(s.sum_up(100-1))
