class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for p in prices[1:]:
            buy_price = min(p, buy_price)
            max_profit = max(max_profit, p - buy_price)

        return max_profit