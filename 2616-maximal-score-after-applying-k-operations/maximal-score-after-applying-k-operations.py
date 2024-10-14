class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        score = 0
        while k:
            max_num = -heapq.heappop(max_heap)
            score += max_num
            new_value = math.ceil(max_num / 3)
            heapq.heappush(max_heap, -new_value)
            k-=1
        
        return score