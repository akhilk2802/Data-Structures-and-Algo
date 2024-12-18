from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        return [num for num, freq in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]




        