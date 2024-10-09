class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        @cache
        def iterate(i, canBuy, coolDownRem):
            if i == len(prices):
                return 0
            
            coolDown = skip = do = 0
            if coolDownRem != 0:
                coolDown = iterate(i + 1, canBuy, coolDownRem - 1)
            else:
                skip = iterate(i + 1, canBuy, coolDownRem)
                if canBuy:
                    do = iterate(i + 1, False, coolDownRem) - prices[i]
                else:
                    do = iterate(i + 1, True, coolDownRem + 1) + prices[i]
            
            return max(coolDown, skip, do)

        return iterate(0, True, 0)