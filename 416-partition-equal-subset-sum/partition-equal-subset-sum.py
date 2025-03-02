class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 1, 5, 11, 5
        # sum = 22
        # total = sum // 2
        # algo - 
        # basically i need to find a subset whose sum is 11
        # if thats not possible, return false

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                # if (t + nums[i]) == target:
                #     return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False