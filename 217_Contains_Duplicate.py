from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numbers = defaultdict(int)

        for value in nums:
            numbers[value] += 1

        occurances = set(numbers.values())

        if len(occurances) == 1 and 1 in occurances:
            return False
        else:
            return True




