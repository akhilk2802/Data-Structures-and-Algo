class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        '''
        [1,2,3,4]
        [1,2,1,1,2,1,2]
        dp
        d = 1
        [1,2,1,1,2,1,2]
        [1,2,3,3,4,5,6]
        odd - 4
        even - 3
        '''
        res = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            res = max(res, cnt)
        return res

