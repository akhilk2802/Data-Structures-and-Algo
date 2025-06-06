class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0 

        min_price = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            max_profit = max((prices[i] - min_price), max_profit)
            min_price = min(prices[i], min_price)

        return max_profit