class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        # Approach -> 
        # brute force approach would be like - 
        # traverse the coins array in reverse-> 
        # check if the coin value is less than amount, if it is, then i want to decrease the value of coin from amount
        # keep doing this untill i reach amount == 0, once i reach amount == 0, increase the count by 1
        # keep doing this untill i complete all the combinations
        # 
        # 
        # 
        cache = {}

        def dfs(index, a):
            if (index, a) in cache:return cache[(index,a)]
            if index == len(coins):
                return 0
            if a > amount:
                return 0
            if a == amount:
                return 1

            cache[(index, a)] = dfs(index, a + coins[index]) + dfs(index + 1, a)
            return cache[(index, a)]

        return dfs(0, 0)