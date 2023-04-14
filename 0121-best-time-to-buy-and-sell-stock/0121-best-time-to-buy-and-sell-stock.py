class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buyP = prices[0]
        
        for currPrice in prices:
            if currPrice < buyP:
                buyP = currPrice
            maxP = max(maxP, currPrice - buyP)
            
        return maxP

        # # left=buy index, right=sell index
        # # two-pointers
        # l, r = 0, 1
        # maxProfit = 0
        # while r < len(prices):
        #     if prices[l] > prices[r]:
        #         l = r
        #     maxProfit = max(maxProfit, prices[r] - prices[l])
        #     r += 1
        # return maxProfit
        