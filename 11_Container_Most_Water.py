class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        area_lst = []
        left = 0
        right = n - 1

        while left <= right:
            difference = abs(height[left] - height[right])
            width = abs(left - right)
            area = (max(height[left], (height[right])) - difference) * width
            area_lst.append(area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max(area_lst)
