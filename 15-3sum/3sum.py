class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            value = -nums[i]
            l, r = i + 1, n - 1

            while l < r:
                total = nums[l] + nums[r]

                if total == value:
                    ans.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif total > value:
                    r -= 1
                else:
                    l += 1

        return ans