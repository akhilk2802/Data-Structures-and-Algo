class Solution:

    def recurPermute(self, index: int, nums: List[int], ans: List[List[int]]):
        if index == len(nums):
            ans.append(nums[:])
            return 

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.recurPermute(index + 1, nums, ans)
            nums[index], nums[i] = nums[i], nums[index]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recurPermute(0, nums, self.ans)
        return self.ans
        