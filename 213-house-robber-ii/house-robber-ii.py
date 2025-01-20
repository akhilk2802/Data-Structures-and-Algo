class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(houses):
            prev2 = 0
            prev = 0
            for house in houses:
                current = max(prev, prev2 + house)
                prev2 = prev
                prev = current
            return prev
        
        n = len(nums)

        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        case1 = rob_linear(nums[1:])
        case2 = rob_linear(nums[:-1])

        return max(case1, case2)

