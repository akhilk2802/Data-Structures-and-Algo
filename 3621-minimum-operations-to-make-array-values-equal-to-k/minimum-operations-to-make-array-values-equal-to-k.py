class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        m = {}
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                if num in m:
                    m[num] += 1
                else:
                    m[num] = 1

        return len(m)
        