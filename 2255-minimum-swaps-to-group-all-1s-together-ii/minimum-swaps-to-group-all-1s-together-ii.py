class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        c1 = sum(nums)
        if c1 <= 1:
            return 0

        extend_nums = nums + nums

        current_ones = sum(extend_nums[:c1])
        # print("current ones : ", nums[:c1])
        max_ones = current_ones

        for i in range(c1, len(extend_nums)):
            current_ones += extend_nums[i] - extend_nums[i - c1]
            max_ones = max(max_ones, current_ones)

        print("C1 : ", c1)

        return c1 - max_ones
