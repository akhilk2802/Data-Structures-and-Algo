class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        global_max = nums[0]

        for i in range(1, n):
            current = nums[i]

            temp_max = max(current, max_so_far * current, min_so_far * current)
            min_so_far = min(current, max_so_far * current, min_so_far * current)
            max_so_far = temp_max

            global_max = max(global_max, max_so_far)

        return global_max
        