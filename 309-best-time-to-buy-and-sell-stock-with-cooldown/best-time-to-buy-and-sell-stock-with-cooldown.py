class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        # bottoms up dp
        dp = [[0] * 2 for _ in range(len(prices) + 2)]

        for cur in range(len(prices) - 1, -1, -1):
            for canBuy in [0, 1]:
                skip = dp[cur + 1][canBuy]
                if canBuy:
                    do = dp[cur + 1][0] - prices[cur]
                else:
                    do = dp[cur + 2][1] + prices[cur]
                dp[cur][canBuy] = max(skip, do)
        
        return dp[0][1]

        # @cache
        # def iterate(i, canBuy):
        #     if i >= len(prices):
        #         return 0
            
        #     skip = iterate(i + 1, canBuy)
        #     if canBuy:
        #         do = iterate(i + 1, False) - prices[i]
        #     else:
        #         do = iterate(i + 2, True) + prices[i]
            
        #     return max(skip, do)

        # return iterate(0, True)