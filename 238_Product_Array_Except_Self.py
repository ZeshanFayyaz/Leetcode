class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left_arr = [1] * n
        right_arr = [1] * n

        for i in range(1, n):
            left_arr[i] = nums[i - 1] * left_arr[i - 1]

        right_arr[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right_arr[i] = nums[i + 1] * right_arr[i + 1]

        answer = [1] * n
        for i in range(n):
            answer[i] = right_arr[i] * left_arr[i]

        return answer


