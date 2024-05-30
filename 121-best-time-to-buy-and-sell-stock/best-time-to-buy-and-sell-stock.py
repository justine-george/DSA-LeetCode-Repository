class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for cur_price in prices[1:]:
            if buy_price > cur_price:
                buy_price = cur_price
            
            max_profit = max(max_profit, cur_price - buy_price)

        return max_profit