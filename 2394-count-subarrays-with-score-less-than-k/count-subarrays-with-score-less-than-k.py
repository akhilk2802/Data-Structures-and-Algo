class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        p = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            p[i+1] = p[i] + nums[i]

        l = 0
        ans = 0

        for r in range(len(nums)):
            while l <= r and (p[r + 1] - p[l]) * (r - l + 1) >= k:
                l += 1

            ans += (r - l + 1)  # this is the trick part in this solution 

        # print("ans -> ", ans)
        return ans