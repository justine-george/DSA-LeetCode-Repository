class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # return max profit possible starting at index i
        # cache = defaultdict(int)
        # def dp(i, isHolding):
        #     if i == len(prices):
        #         return 0
            
        #     if (i, isHolding) in cache:
        #         return cache[(i, isHolding)]
            
        #     # do nothing
        #     profit_doNothing = dp(i + 1, isHolding)

        #     # do something
        #     profit_doSomething = 0
        #     if isHolding:
        #         profit_doSomething = prices[i] + dp(i + 1, False)
        #     else:
        #         profit_doSomething = -prices[i] + dp(i + 1, True)
            
        #     cache[(i, isHolding)] = max(profit_doNothing, profit_doSomething)
        #     return cache[(i, isHolding)]

        # return dp(0, False)

        # greedy approach
        # sell if previous value is less than current (simulating a buy and sell transaction)

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


