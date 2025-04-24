class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        distinct = len(set(nums))
        n = len(nums)
        result = 0
        m = {}
        r = 0

        for l in range(n):
            while r < n and len(m) < distinct:
                add = nums[r]
                m[add] = m.get(add, 0) + 1
                r += 1

            if len(m) == distinct:
                result += n - r + 1

            m[nums[l]] -= 1
            if m[nums[l]] == 0:
                del m[nums[l]]

        return result
        

        '''
        brute force method ->
        '''

        # total_distinct = len(set(nums))
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     for j in range(i, n + 1):
        #         # print("nums subarray => ", nums[i:j])
        #         distinct_elements_subarray = len(set(nums[i:j]))

        #         if distinct_elements_subarray == total_distinct:
        #             count += 1

        # return count