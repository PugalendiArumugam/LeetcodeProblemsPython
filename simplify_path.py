# 71 Simplify path
# Example 1:
# Input: path = "/home/"
# Output: "/home"
# Explanation:
# The trailing slash should be removed.
#
# Example 2:
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation:
# Multiple consecutive slashes are replaced by a single one.
#
# Example 3:
# Input: path = "/home/user/Documents/../Pictures"
# Output: "/home/user/Pictures"
# Explanation:
# A double period ".." refers to the directory up a level (the parent directory).
#
# Example 4:
# Input: path = "/../"
# Output: "/"
# Explanation:
# Going one level up from the root directory is not possible.
#
# Example 5:
# Input: path = "/.../a/../b/c/../d/./"
# Output: "/.../b/d"
# Explanation:
# "..." is a valid name for a directory in this problem.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if not part or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        result = '/' + '/'.join(stack)
        return result

s=Solution()
print(s.simplifyPath('/home/'))
print(s.simplifyPath('/home//foo/'))
print(s.simplifyPath('/home/user/Documents/../Pictures'))
print(s.simplifyPath('/../'))
print(s.simplifyPath('/.../a/../b/c/../d/./'))
