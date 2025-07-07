# 166. Fraction to Recurring Decimal
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        result = []
        is_negative = (numerator > 0) ^ (denominator > 0)
        if is_negative:
            result.append('-')
        x = abs(numerator)
        y = abs(denominator)
        result.append(str(x // y))
        rem = x % y
        if rem == 0:
            return ''.join(result)
        result.append('.')
        seen_remainders = {}
        while rem != 0:
            if rem in seen_remainders:
                idx = seen_remainders[rem]
                result.insert(idx, '(')
                result.append(')')
                break
            seen_remainders[rem] = len(result)
            rem *= 10
            result.append(str(rem // y))
            rem %= y

        return ''.join(result)


s=Solution()
print(s.fractionToDecimal(1,2))
print(s.fractionToDecimal(2,1))
print(s.fractionToDecimal(10,3))
print(s.fractionToDecimal(4,333))
