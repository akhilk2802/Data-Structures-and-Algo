class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefix_sum = 0
        prefix_count = {0:1}

        for num in nums:
            prefix_sum += num
            val = prefix_sum - k
            if val in prefix_count:
                count += prefix_count[val]

            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1

        return count