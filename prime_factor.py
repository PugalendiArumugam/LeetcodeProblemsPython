import math
# The prime factors of  are  and .
# What is the largest prime factor of a given number ?

# Input Format
# First line contains , the number of test cases. This is followed by  lines each containing an integer .

# input
# 2
# 10
# 17

# Output
# 5
# 17

class Solution:
    def max_prime(self,n): 
        if n<=2: return 0 
        maxPrime = -1
        while n % 2 == 0: 
            maxPrime = 2
            n >>= 1 
    
        for i in range(3, int(math.sqrt(n)) + 1, 2): 
            while n % i == 0: 
                maxPrime = i 
                n //= i 

        return n if n > 2 else maxPrime
  
if __name__ == "__main__":
    s = Solution()
    print(s.max_prime(2))
    print(s.max_prime(10))
    print(s.max_prime(17))
