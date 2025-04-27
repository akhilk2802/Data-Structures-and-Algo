class Solution:
    def countSubarrays(self, nums: List[int]) -> int:


        start = 0
        end = 2
        count = 0
        n = len(nums)
        
        while end < n:
            if (nums[start] + nums[end]) * 2 == nums[start + 1]:
                count += 1

            start += 1
            end += 1
        
        return count


        # count = 0
        # n = len(nums)

        # for i in range(n-2):
        #     j = i + 1
        #     k = i + 2

        #     if nums[i] + nums[k] == nums[j] / 2:
        #         count += 1

        # return count