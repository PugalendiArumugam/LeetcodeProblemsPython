# Example 1:
# Input: s = "0"
# Output: true
#
# Example 2:
# Input: s = "e"
# Output: false
#
# Example 3:
# Input: s = "."
# Output: false
# valid numbers
# "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789",

# invalid numbers
# abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

class Solution:
    def isNumber(self, s: str) -> bool:
        length = len(s)
        index = 0
        pre_signed=False
        if s[index] in '+-':
            index += 1
            pre_signed=True
        if index == length:
            return False
        if s[index] == '.' and (index + 1 == length or s[index + 1] in 'eE'):
            return False
        dot_count = exponent_count = 0
        while index < length:
            if s[index] == '.':
                if exponent_count or dot_count:
                    return False
                dot_count += 1
            elif s[index] in 'eE':
                if exponent_count or index == 0 or index == length - 1 or (index==1 and pre_signed):
                    return False
                exponent_count += 1
                if s[index + 1] in '+-':
                    index += 1
                    if index == length - 1:
                        return False
            elif not s[index].isdigit():
                return False
            index += 1
        return True


    def isNumber2(self, s: str) -> bool:
        # Length of the input string.
        length = len(s)
        # Start index for traversing the string.
        index = 0

        # Check for optional sign at the beginning.
        if s[index] in '+-':
            index += 1

        # Empty string after a sign or no numeric part is invalid.
        if index == length:
            return False

        # Single dot without digits or dot directly followed by exponent is invalid.
        if s[index] == '.' and (index + 1 == length or s[index + 1] in 'eE'):
            return False

        # Counters for dots and exponent characters.
        dot_count = exponent_count = 0

        # Traverse the string starting from the current index.
        while index < length:
            if s[index] == '.':
                # If there's already a dot or an exponent, it's invalid.
                if exponent_count or dot_count:
                    return False
                dot_count += 1
            elif s[index] in 'eE':
                # If there's already an exponent, or this is the first character, or there isn't a number following, it's invalid.
                if exponent_count or index == 0 or index == length - 1:
                    return False
                exponent_count += 1
                # Check for an optional sign after the exponent.
                if s[index + 1] in '+-':
                    index += 1
                    # If the string ends after the sign, it's invalid.
                    if index == length - 1:
                        return False
            # Non-numeric, non-dot, and non-exponent characters are invalid.
            elif not s[index].isdigit():
                return False
            index += 1

        # If all checks pass, the string represents a valid number.
        return True


s=Solution()
print(s.isNumber('0')) #true
print(s.isNumber('e')) #false
print(s.isNumber('.')) #false
print(s.isNumber('-0.1')) #true
print(s.isNumber('-90E3')) #true
print(s.isNumber('3e+7')) #true
print(s.isNumber('-123.456e789')) #true
print(s.isNumber('1e'))  #false
print(s.isNumber('99e2.5')) #false
print(s.isNumber('-+3')) #false
print(s.isNumber('95a54e53')) #false
print(s.isNumber('+E3')) #false    // failed
