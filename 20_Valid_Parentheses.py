class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        opened = ['(', '{', '[']
        closed = [')', '}', ']']

        if len(s) == 0 or len(s) % 2 != 0:
            return False

        else:
            for char in s:
                if char in opened:
                    stack.append(char)
                else:
                    if not stack:
                        return False
                    if stack[-1] == opened[closed.index(char)]:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

