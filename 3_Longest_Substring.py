class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        max_length = 0
        left = 0
        right = 0

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
        return max_length
