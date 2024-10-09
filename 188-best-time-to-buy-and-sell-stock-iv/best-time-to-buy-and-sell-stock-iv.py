class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        # bottoms up dp
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(len(prices) + 1)]

        for cur in range(len(prices) - 1, -1, -1):
            for canBuy in [0, 1]:
                for rem in range(1, k + 1):
                    skip = dp[cur + 1][canBuy][rem]
                    if canBuy:
                        do = dp[cur + 1][0][rem] - prices[cur]
                    else:
                        do = dp[cur + 1][1][rem - 1] + prices[cur]
                    dp[cur][canBuy][rem] = max(skip, do)
        
        return dp[0][1][k]
        
        # @cache
        # def get_max_profit(cur, canBuy, remaining):
        #     if cur == len(prices) or remaining == 0:
        #         return 0
            
        #     skip = get_max_profit(cur + 1, canBuy, remaining)
        #     if canBuy:
        #         do = get_max_profit(cur + 1, False, remaining) - prices[cur]
        #     else:
        #         do = get_max_profit(cur + 1, True, remaining - 1) + prices[cur]

        #     return max(skip, do)

        # return get_max_profit(0, True, k)