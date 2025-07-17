# 316 Remove duplicate letters
#
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Example 1:
# Input: s = "bcabc"
# Output: "abc"
#
# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"
#
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_item = {char: _ for _, char in enumerate(s)}
        # since this is set.  This will result in last index of the value updated in sorted order
        # eg1. 'baabbbaabbccccd' will be generated as  {'a': 7, 'b': 9, 'c': 13, 'd': 14} .
        # but we want it in a lexicographical order.
        # eg2. "cbacdcbc" as {'a': 2, 'b': 6, 'c': 7, 'd': 4}
        #
        stack = []
        visited = set()
        # iterate thru original string, and store in a stack if it is not visited already
        # top element in the stack greater than the current character
        # and top element count is more than one in
        for index, char in enumerate(s):
            if char in visited:
                continue
            while stack and stack[-1] > char and last_item[stack[-1]] > index:
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)
        return ''.join(stack)

    def removeDuplicateLetters3(self, s: str) -> str:
        # Create a dictionary to store the last occurrence of each character
        last_occurrence = {char: index for index, char in enumerate(s)}

        # Initialize an empty stack to keep track of the characters in result
        stack = []

        # Set to keep track of characters already in the stack to avoid duplicates
        visited = set()

        # Iterate over each character and its index in the string
        for index, char in enumerate(s):
            # Skip if the character is already in the visited set
            if char in visited:
                continue

            # Ensure the top element of the stack is greater than the current character
            # and the top element occurs later in the string as well
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > index:
                # The top element can be removed and thus it is no longer visited.
                visited.remove(stack.pop())

            # Add the current character to the stack and mark it as visited
            stack.append(char)
            visited.add(char)

        # Convert the stack to a string by joining the characters
        return ''.join(stack)

s=Solution()
# print(s.removeDuplicateLetters('baabbbaabbccccd'))
# print(s.removeDuplicateLetters("bcabc"))
#print(s.removeDuplicateLetters("cbacdcbc"))
print(s.removeDuplicateLetters("zadcbaa"))
