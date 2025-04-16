class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        freq = defaultdict(int)
        left = 0
        pairs = 0
        good_sub = 0

        for right in range(len(nums)):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while pairs >= k:
                good_sub += len(nums) - right
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return good_sub