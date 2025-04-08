class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        def recur(arr):
            arr_set = set(arr)
            if len(arr_set) == len(arr):
                return 0

            return 1 + recur(arr[3:])

        count = recur(nums)
        # print("count -> ", count)
        return count
