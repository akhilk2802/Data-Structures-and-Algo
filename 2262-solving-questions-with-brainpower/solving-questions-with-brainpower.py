class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)
        memo = {}

        def dfs(i):
            
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            take = questions[i][0] + dfs(i + questions[i][1] + 1)
            skip = dfs(i + 1)

            memo[i] = max(take, skip)
            return memo[i]

        return dfs(0)


        '''
        brute force ->
        '''
        # n = len(questions)
        # max_result = 0

        # for i in range(n):
        #     j = i
        #     points = 0
        #     while j < n:
        #         points += questions[j][0]
        #         j += (questions[j][1] + 1)
        #     max_result = max(max_result, points)

        # return max_result

