from collections import defaultdict
import heapq

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def digitSum(n):
            return sum(map(int, str(n)))  # Faster digit sum calculation

        m = defaultdict(list)

        for n in nums:
            val = digitSum(n)
            if len(m[val]) < 2:
                heapq.heappush(m[val], n)  # Push directly without negation
            else:
                heapq.heappushpop(m[val], n)  # Maintain top 2 largest values only

        maxSum = -1

        for key in m:
            if len(m[key]) == 2:  # Only process pairs
                maxSum = max(maxSum, sum(m[key]))

        return maxSum