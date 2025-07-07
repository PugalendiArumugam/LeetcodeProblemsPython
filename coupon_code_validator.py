# 3606. Coupon Code Validator
# You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:
#
# code[i]: a string representing the coupon identifier.
# businessLine[i]: a string denoting the business category of the coupon.
# isActive[i]: a boolean indicating whether the coupon is currently active.
# A coupon is considered valid if all of the following conditions hold:
#
# code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
# businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
# isActive[i] is true.
# Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics",
# "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

# Example 1:
# Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]
# Output: ["PHARMA5","SAVE20"]
# Explanation:
# First coupon is valid.
# Second coupon has empty code (invalid).
# Third coupon is valid.
# Fourth coupon has special character @ (invalid).
#
# Example 2:
# Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]
# Output: ["ELECTRONICS_50"]
# Explanation:
# First coupon is inactive (invalid).
# Second coupon is valid.
# Third coupon has invalid business line (invalid).
from typing import List
import string
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result=[]
        list_len=len(code)
        valid_business=["electronics", "grocery", "pharmacy", "restaurant"]
        for i in range(0,list_len):
            curr_code=code[i]
            curr_buss=businessLine[i]
            is_active=isActive[i]
            if curr_buss not in valid_business: continue
            if not is_active: continue
            if len(curr_code) == 0: continue
            special_char=False
            for c in curr_code:
                if not (c.isalpha() or c.isdigit() or c == '_'):
                    special_char=True
                    break
            if special_char: continue
            result.append((curr_buss, curr_code))

        result.sort()
        return [x for _,x in result]

s=Solution()
print(s.validateCoupons(["SAVE20","","PHARMA5","SAVE@20"],["restaurant","grocery","pharmacy","restaurant"],[True,True,True,True]))
print(s.validateCoupons(["GROCERY15","ELECTRONICS_50","DISCOUNT10"],["grocery","electronics","invalid"],[False,True,True]))
