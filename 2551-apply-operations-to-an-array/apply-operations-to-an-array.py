class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        # Algo -> 
        # 1. one pass
        # 2. keep updating the array with the operations 
        # 3. perform swap operation to put all the zeros to the end 
        # 4. will have to use two for loops

        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i]
                nums[i + 1] = 0

        l = 0
        r = l + 1
        while r < n:
            if nums[r] > 0 and nums[l] == 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            elif nums[l] > 0:
                l += 1
            r += 1

        return nums
            