class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        buy_price = prices[0]
        for cur_price in prices[1:]:
            if cur_price < buy_price:
                buy_price = cur_price
            max_profit = max(max_profit, cur_price - buy_price)
        return max_profit