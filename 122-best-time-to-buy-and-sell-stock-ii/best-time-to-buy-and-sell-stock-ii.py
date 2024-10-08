class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(len(prices) - 1):
            profit = 0
            if prices[i + 1] >= prices[i]:
                profit = prices[i + 1] - prices[i]
            total_profit += profit
        return total_profit