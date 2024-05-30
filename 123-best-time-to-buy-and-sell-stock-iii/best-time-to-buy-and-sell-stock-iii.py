class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # return max profit possible starting at index i
        @cache
        def dp(i, k, isHolding):
            if i == len(prices) or k == 0:
                return 0
            
            # do nothing
            doNothing = dp(i + 1, k, isHolding)

            # do something
            doSomething = 0
            if isHolding:
                doSomething = prices[i] + dp(i + 1, k - 1, False)
            else:
                doSomething = -prices[i] + dp(i + 1, k, True)
            
            max_profit = max(doNothing, doSomething)
            return max_profit



        return dp(0, 2, False)