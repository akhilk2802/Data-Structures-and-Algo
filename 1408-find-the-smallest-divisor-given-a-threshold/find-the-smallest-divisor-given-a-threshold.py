class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        '''
        nums = [1,2,5,9]
        threshold = x 
        search range => 1 to max(nums)
        '''
        def compare(k):

            val = 0
            for num in nums:
                val += (num + k - 1) // k
            # print("val and k: ", val, k)
            return val <= threshold

        low, high = 1, max(nums)

        while low < high:

            mid = (low + high) // 2

            if compare(mid):
                high = mid
            else:
                low = mid + 1

        return low