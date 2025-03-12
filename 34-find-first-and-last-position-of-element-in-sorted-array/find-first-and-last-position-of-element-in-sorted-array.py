class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findLast(nums):

            low = 0
            high = len(nums) - 1
            last = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return last

        def findFirst(nums):

            low = 0
            high = len(nums) - 1
            first = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return first

        return [findFirst(nums), findLast(nums)]
        