class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for p in prices[1:]:
            if p < buy_price:
                buy_price = p
            max_profit = max(max_profit, p - buy_price)

        return max_profit