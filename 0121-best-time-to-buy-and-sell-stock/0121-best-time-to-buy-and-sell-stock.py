class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buyP = prices[0]
        for currPrice in prices:
            if currPrice < buyP:
                buyP = currPrice
            maxP = max(maxP, currPrice - buyP)
        return maxP
        