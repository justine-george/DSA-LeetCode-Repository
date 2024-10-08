class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state variables
        if not prices:
            return 0
        
        A = -prices[0]
        B = float('-inf')
        C = float('-inf')
        D = float('-inf')

        for price in prices:
            A = max(A, -price)
            B = max(B, A + price)
            C = max(C, B - price)
            D = max(D, C + price)
            
        return D
        
        # memo = {}
        # def iterate(i, canBuy, rem):
        #     if (i, canBuy, rem) in memo:
        #         return memo[(i, canBuy, rem)]
                
        #     if i >= len(prices) or rem == 0:
        #         return 0

        #     if canBuy:
        #         buy = iterate(i + 1, False, rem) - prices[i]
        #         skip = iterate(i + 1, True, rem)
        #         res = max(buy, skip)
        #     else:
        #         sell = iterate(i + 1, True, rem - 1) + prices[i]
        #         skip = iterate(i + 1, False, rem)
        #         res = max(sell, skip)
            
        #     memo[(i, canBuy, rem)] = res
        #     return res

        # return iterate(0, True, 2)