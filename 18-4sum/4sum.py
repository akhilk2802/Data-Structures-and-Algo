class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        '''
        Since the order does not matter - i can sort the given array and perform operations on them
        [-2,-1,0,0,1,2]

        '''

        nums = sorted(nums)
        n = len(nums)
        result = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result

        # n = len(nums)
        # quads = set()

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j + 1, n):
        #             for l in range(k + 1, n):
        #                 if nums[i] + nums[j] + nums[k] + nums[l] == target:
        #                     quads.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))

        # return list(quads)  
        