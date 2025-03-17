class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        '''
        Brute force approach -> sort things out 
        maintain the count
        as you go with the for loop after sorting
        keep increasing the count if two values are equal 
        '''

        # count = Counter(nums)
        # for c in count.values():
        #     if c % 2 != 0:
        #         return False
        # return True

        n = len(nums) // 2
        nums.sort()
        count = 0

        for i in range(1, len(nums), 2):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                return False

        return count == n