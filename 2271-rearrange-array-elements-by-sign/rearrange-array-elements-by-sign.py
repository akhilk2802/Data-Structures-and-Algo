class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pos = []
        neg = []

        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        i, j = 0, 0
        result = []
        while i < n//2:
            result.append(pos[i])
            result.append(neg[i])
            i+=1

        return result