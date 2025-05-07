from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = defaultdict(int)

        for n in nums:
            occurances[n] += 1

        occurances = dict(sorted(occurances.items(), key=lambda x: x[1], reverse=True))

        return (list(occurances.keys())[:k])
