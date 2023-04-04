class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buyP = prices[0]
        for price in prices:
            if price < buyP:
                buyP = price
            maxP = max(maxP, price - buyP)
        return maxP
        