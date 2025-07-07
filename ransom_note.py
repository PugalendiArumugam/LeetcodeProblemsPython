from collections import Counter
# 383 Ransome note
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        char_counter=Counter(magazine)

        for char in ransomNote:
            char_counter[char] -=1

            if char_counter[char]<0:
                return False
            
        return True

    # Fastest and different approach
    def canConstruct(self, ransomNote, magazine):
        alphabet = [0] * 26
        for c in ransomNote:
            idx = ord(c) - ord('a')
            i = magazine.find(c, alphabet[idx])
            if i == -1:
                return False
            alphabet[idx] = i + 1
        return True

if __name__ == '__main__':
    s=Solution()
    result = s.canConstruct("a","b")
    print(result)
    result=s.canConstruct("aa","ab")
    print(result)
    result=s.canConstruct2("aa","aab")
    print(result)
