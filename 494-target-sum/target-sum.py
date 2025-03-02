class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        # Approach -
        # 1. 1 + 1 + 1 + 1 - 1 => 3
        # P - N = target
        # P + N = totalSum
        # 2P = target + totalSum
        # P = (target + totalSum)/2
        dp = {}

        def generate(index, currentSum):
            if (index, currentSum) in dp:
                return dp[(index, currentSum)]

            if index == len(nums):
                if currentSum == target:
                    return 1
                else:
                    return 0

            count_positive = generate(index + 1, currentSum + nums[index])
            count_negative = generate(index + 1, currentSum - nums[index])

            dp[(index, currentSum)] = count_negative + count_positive

            return dp[(index, currentSum)]

        return generate(0, 0)