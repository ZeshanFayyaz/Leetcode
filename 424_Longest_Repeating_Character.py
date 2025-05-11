class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        length = 0

        left = 0
        right = 0

        for right in range(len(s)):
            temp = k[right]
            count[temp] = 1 + count.get(temp, 0)

            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)
        return length


