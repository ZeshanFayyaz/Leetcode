class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums = sorted(nums)

        if (len(nums) == 3):
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        elif (len(nums) < 3):
            return []
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                j = i + 1
                k = len(nums) - 1

                while j < k:
                    total = nums[j] + nums[k] + nums[i]
                    if total == 0:
                        ans.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif total < 0:
                        j += 1
                    else:
                        k -= 1

        final = set()
        lst = []

        for item in ans:
            temp = tuple(item)
            if temp not in final:
                final.add(temp)
                lst.append(temp)

        return (lst)


