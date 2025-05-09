from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        print("count -> ", count)

        min_heap = []

        for num, freq in count.items():
            # print("num and freq -> ", num, freq)
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # print("min_heap -> ", min_heap)
        result = []

        for freq, num in min_heap:
            result.append(num)

        return result