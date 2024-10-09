class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        @cache
        def iterate(i, canBuy):
            if i >= len(prices):
                return 0
            
            skip = iterate(i + 1, canBuy)
            if canBuy:
                do = iterate(i + 1, False) - prices[i]
            else:
                do = iterate(i + 2, True) + prices[i]
            
            return max(skip, do)

        return iterate(0, True)