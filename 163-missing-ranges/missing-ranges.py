class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        result = []
        prev = lower - 1
        nums.append(upper + 1)

        for num in nums:
            if num - prev >= 2:
                result.append([prev + 1, num - 1])
            prev = num
        
        return result

        