class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        if N <= 1:
            return 0

        @cache
        def iterate(i, canBuy):
            if i >= N:
                return 0
            
            skip = iterate(i + 1, canBuy)
            if canBuy:
                do = iterate(i + 1, False) - prices[i]
            else:
                do = iterate(i + 1, True) + prices[i] - fee
            return max(skip, do)

        return iterate(0, True)