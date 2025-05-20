from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        min_heap = []

        for key, value in count.items():
            heappush(min_heap, (value, key))

            while len(min_heap) > k:
                heappop(min_heap)

        # print("heap -> ", min_heap)
        result = []
        for key, value in min_heap:
            # print("values -> ", value)
            result.append(value)
        
        return result