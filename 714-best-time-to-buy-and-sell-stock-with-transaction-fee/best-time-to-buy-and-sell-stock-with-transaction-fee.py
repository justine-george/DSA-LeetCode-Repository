class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        if N <= 1:
            return 0
        
        dp = [[0] * 2 for _ in range(N + 1)]

        for cur in range(N - 1, -1, -1):
            for canBuy in [0, 1]:
                skip = dp[cur + 1][canBuy]
                if canBuy:
                    do = dp[cur + 1][0] - prices[cur]
                else:
                    do = dp[cur + 1][1] + prices[cur] - fee
                dp[cur][canBuy] = max(do, skip)

        return dp[0][1]
        

        # @cache
        # def iterate(i, canBuy):
        #     if i >= N:
        #         return 0
            
        #     skip = iterate(i + 1, canBuy)
        #     if canBuy:
        #         do = iterate(i + 1, False) - prices[i]
        #     else:
        #         do = iterate(i + 1, True) + prices[i] - fee
        #     return max(skip, do)

        # return iterate(0, True)