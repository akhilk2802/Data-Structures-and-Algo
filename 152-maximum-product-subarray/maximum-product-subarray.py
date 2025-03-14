class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_so_far = min_so_far = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far

            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)

            result = max(result, max_so_far)

        return result

        