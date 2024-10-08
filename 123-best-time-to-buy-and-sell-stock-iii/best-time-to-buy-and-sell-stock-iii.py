class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
    
        n = len(prices)
        transactions = 2

        # Initialize the dp array
        dp = [[[0] * (transactions + 1) for _ in range(2)] for _ in range(n + 1)]
        
        # Fill the dp array
        for i in range(n - 1, -1, -1):  # start from the last day
            for canBuy in range(2):
                for rem in range(1, transactions + 1):  # rem value from 1 to transactions
                    skipProfit = dp[i + 1][canBuy][rem]  # No transaction on day i
                    if canBuy:
                        doProfit = dp[i + 1][0][rem] - prices[i]  # Buy option
                    else:
                        doProfit = dp[i + 1][1][rem - 1] + prices[i]  # Sell option
                    
                    # Select the maximum profit for the state (i, canBuy, rem)
                    dp[i][canBuy][rem] = max(skipProfit, doProfit)
        
        # Result is starting from day 0, with the ability to buy, and full transactions available
        return dp[0][1][2]
        
        '''
        memo = {}
        def iterate(i, canBuy, rem):
            if i >= len(prices) or rem == 0:
                return 0
            if (i, canBuy, rem) in memo:
                return memo[(i, canBuy, rem)]
                
            skipProfit = iterate(i + 1, canBuy, rem)
            if canBuy:
                doProfit = iterate(i + 1, False, rem) - prices[i]
            else:
                doProfit = iterate(i + 1, True, rem - 1) + prices[i]
            memo[(i, canBuy, rem)] = max(skipProfit, doProfit)
            
            return memo[(i, canBuy, rem)]

        return iterate(0, True, 2)
        '''

        # # state variables
        # if not prices:
        #     return 0
        
        # A = -prices[0]
        # B = float('-inf')
        # C = float('-inf')
        # D = float('-inf')

        # for price in prices:
        #     A = max(A, -price)
        #     B = max(B, A + price)
        #     C = max(C, B - price)
        #     D = max(D, C + price)
            
        # return D