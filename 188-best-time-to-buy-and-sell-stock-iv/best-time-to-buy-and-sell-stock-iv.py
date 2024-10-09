class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        @cache
        def get_max_profit(cur, canBuy, remaining):
            if cur == len(prices) or remaining == 0:
                return 0
            
            skip = get_max_profit(cur + 1, canBuy, remaining)
            if canBuy:
                do = get_max_profit(cur + 1, False, remaining) - prices[cur]
            else:
                do = get_max_profit(cur + 1, True, remaining - 1) + prices[cur]

            res = max(skip, do)

            return res
        return get_max_profit(0, True, k)