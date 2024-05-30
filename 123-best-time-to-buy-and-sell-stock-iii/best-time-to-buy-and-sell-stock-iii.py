class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # return max profit possible starting at index i
        cache = defaultdict(int)
        def dp(i, k, isHolding):
            if i == len(prices) or k == 0:
                return 0
            
            if (i, k, isHolding) in cache:
                return cache[(i, k, isHolding)]
            
            # do nothing
            profit_doNothing = dp(i + 1, k, isHolding)

            # do something
            profit_doSomething = 0
            if isHolding:
                profit_doSomething = prices[i] + dp(i + 1, k - 1, False)
            else:
                profit_doSomething = -prices[i] + dp(i + 1, k, True)
            
            cache[(i, k, isHolding)] = max(profit_doNothing, profit_doSomething)
            return cache[(i, k, isHolding)]

        return dp(0, 2, False)