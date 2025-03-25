class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_price = float("inf")

        for i in range(len(prices)):
            max_profit = max(prices[i] - min_price, max_profit)
            min_price = min(min_price, prices[i])

        return max_profit