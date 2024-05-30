class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if buyPrice > prices[i]:
                buyPrice = prices[i]
            
            max_profit = max(max_profit, prices[i] - buyPrice)

        return max_profit