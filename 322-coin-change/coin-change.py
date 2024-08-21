class Solution:
    '''
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

    Aim: Return the fewest number of coins that you need to make up that amount.

    If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.

    Example:
    coins = [1,2,5]
    amount = 11

    use min number of coins to make up amount
    amount gets reduced

    11 remaining
        10 with 1, 9 with 1, 6 with 1

    amount remaining
        global min = float('inf')
        consider each coin:
            find out min coins with this amount
            find the global min for this amount
        return global min
    '''

    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def minCoins(remaining):
            if remaining < 0:
                return float('inf')
            if remaining == 0:
                return 0

            min_for_amount = float('inf')
            for coin in coins:
                current_min = minCoins(remaining - coin)
                if current_min != float('inf'):
                    min_for_amount = min(current_min + 1, min_for_amount)
            return min_for_amount
        
        res = minCoins(amount)
        return res if res != float('inf') else -1
                