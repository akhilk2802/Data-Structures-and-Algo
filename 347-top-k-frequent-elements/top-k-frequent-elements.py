class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        sorted_counter = [key for key, value in sorted(counter.items(), key=lambda item: item[1],reverse=True)[:k]]

        return sorted_counter[:k]
