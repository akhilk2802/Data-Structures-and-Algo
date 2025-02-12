class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def digitSum(n):
            return sum(map(int, str(n)))

        m = defaultdict(list)

        for n in nums:
            val = digitSum(n)
            if len(m[val]) < 2:
                heapq.heappush(m[val], n)
            else:
                heapq.heappushpop(m[val], n)

        maxSum = -1

        for key in m:
            if len(m[key]) == 2:
                maxSum = max(maxSum, sum(m[key]))

        return maxSum