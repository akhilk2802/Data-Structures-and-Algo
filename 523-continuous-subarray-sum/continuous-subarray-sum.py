class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefix_sum = 0
        prefix_sum_mod_map = {0: -1}  # To handle the case where the subarray starts from index 0

        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k

            if prefix_sum in prefix_sum_mod_map:
                if i - prefix_sum_mod_map[prefix_sum] > 1:
                    return True
            else:
                prefix_sum_mod_map[prefix_sum] = i

        return False
        