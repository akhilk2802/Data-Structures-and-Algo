class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def digitSum(n):
            return sum(int(digit) for digit in str(n))

        m = defaultdict(list)

        for n in nums:
            val = digitSum(n)
            heapq.heappush(m[val], -n)

        maxSum = -1

        for key in m:
            if len(m[key]) >= 2:
                first, second = -heapq.heappop(m[key]), -heapq.heappop(m[key])
                maxSum = max(maxSum, first + second)

        return maxSum