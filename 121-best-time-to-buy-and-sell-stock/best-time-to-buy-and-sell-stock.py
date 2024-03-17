class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]
        
        for price in prices:
            buyPrice = min(buyPrice, price)
            maxProfit = max(maxProfit, price - buyPrice)

        return maxProfit
