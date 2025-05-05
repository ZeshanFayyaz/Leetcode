import string


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = str("".join(char for char in s if char.isalnum()).lower())

        if len(s) <= 1:
            return True
        else:
            left = 0
            right = len(s) - 1

            while left <= right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True


