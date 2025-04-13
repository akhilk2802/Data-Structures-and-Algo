class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = (10 ** 9) + 7
        odd_count = n - n // 2
        even_count = n // 2

        return (pow(5, odd_count, MOD) * pow(4, even_count, MOD)) % MOD

        
        '''
        Below solution gives Max Recursion depth - that is 1000 
        Lets optimise it ->
        '''
        # total = 1
        # MOD = (10 ** 9) + 7

        # def recur(number, t):

        #     if number == 1:
        #         t = (t * 5) % MOD
        #         return t
        #     if number % 2 == 0:
        #         t = (t * 4) % MOD
        #     else:
        #         t = (t * 5) % MOD
        #     return recur(number - 1, t)

        # total = recur(n, total)
        # return total