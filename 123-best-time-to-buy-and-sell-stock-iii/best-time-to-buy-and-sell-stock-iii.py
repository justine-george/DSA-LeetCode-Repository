class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def iterate(i, canBuy, rem):
            if i >= len(prices) or rem == 0:
                return 0
            if (i, canBuy, rem) in memo:
                return memo[(i, canBuy, rem)]
                
            skipProfit = iterate(i + 1, canBuy, rem)
            doProfit = iterate(i + 1, False, rem) - prices[i] if canBuy else iterate(i + 1, True, rem - 1) + prices[i]
            memo[(i, canBuy, rem)] = max(skipProfit, doProfit)
            
            return memo[(i, canBuy, rem)]

        return iterate(0, True, 2)

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