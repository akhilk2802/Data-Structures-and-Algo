class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        nums = []
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums.append(grid[i][j])

        nums.sort()

        len_nums = len(nums)
        common_number = nums[len_nums // 2]

        for num in nums:
            if num % x != common_number % x:
                return -1
            result += abs(common_number - num) // x
        
        return result