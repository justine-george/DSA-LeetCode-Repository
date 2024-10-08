class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def iterate(i, canBuy, rem):
            if i >= len(prices) or rem == 0:
                return 0

            if canBuy:
                buy = iterate(i + 1, False, rem) - prices[i]
                skip = iterate(i + 1, True, rem)
                res = max(buy, skip)
            else:
                sell = iterate(i + 1, True, rem - 1) + prices[i]
                skip = iterate(i + 1, False, rem)
                res = max(sell, skip)
            
            return res

        return iterate(0, True, 2)