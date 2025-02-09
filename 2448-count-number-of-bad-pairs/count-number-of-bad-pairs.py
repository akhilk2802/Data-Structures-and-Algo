class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        gp = 0
        tp = 0
        cp = defaultdict(int)

        for i in range(len(nums)):
            tp += i
            gp += cp[nums[i] - i]
            cp[nums[i]-i] += 1

        return tp - gp
        