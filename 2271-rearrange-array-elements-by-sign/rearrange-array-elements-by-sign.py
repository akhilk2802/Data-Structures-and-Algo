class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        positive_arr = []
        negative_arr = []

        for i in range(len(nums)):
            if nums[i] > 0:
                positive_arr.append(nums[i])
            elif nums[i] < 0:
                negative_arr.append(nums[i])

        result = []
        i, j = 0, 0

        while i < len(positive_arr) and j < len(negative_arr):
            result.append(positive_arr[i])
            result.append(negative_arr[j])
            i+=1
            j+=1
            

        # print("result: ", result)
        return result
        