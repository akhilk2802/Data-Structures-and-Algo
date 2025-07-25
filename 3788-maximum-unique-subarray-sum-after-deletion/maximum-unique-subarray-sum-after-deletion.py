class Solution:
    def maxSum(self, nums: List[int]) -> int:

        m = Counter(nums)
        s = 0

        max_val = max(nums)
        if max_val < 0:
            return max_val
        else:
            for k, _ in m.items():
                s += max(k, 0)
            return s


        # freq_count = Counter(nums)
        # m = -200
        # total = 0

        # for k, v in freq_count.items():
        #     total += k
        #     # total = max(total, 0)
        #     m = max(total, m)

        # return m