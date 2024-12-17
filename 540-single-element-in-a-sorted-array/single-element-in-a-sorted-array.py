class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        counter = {}

        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1

        for num, count in counter.items():
            if count == 1:
                return num

        return -1