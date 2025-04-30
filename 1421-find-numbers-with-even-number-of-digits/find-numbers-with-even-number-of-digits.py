class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        count = 0

        for n in nums:
            str_n = str(n)
            val = len(str_n)
            if val % 2 == 0:
                count += 1

        return count