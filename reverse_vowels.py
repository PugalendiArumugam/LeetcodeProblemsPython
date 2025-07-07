# 345 reverse vowel of the string 
# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) -1
        ans=list(s)
        vowels='AEIOUaeiou'
        while i<j:
            while i < j and ans[i] not in vowels:
               i+=1
            while i < j and ans[j] not in vowels:
               j-=1
            if i < j:
                ans[i],ans[j] = ans[j],ans[i]
                i+=1
                j-=1
        return "".join(ans)


if __name__ == "__main__":
    s = Solution()
    result = s.reverseVowels('IceCreAm')
    print("Result",result)

    result = s.reverseVowels('leetcode')
    print("Result",result)
    
        