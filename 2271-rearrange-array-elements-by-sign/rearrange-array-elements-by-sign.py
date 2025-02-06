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
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            i+=1
            result.append(neg[j])
            j+=1

        return result