class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10,15,20]
        # [2  15 20  0]
        
        dp = cost + [0]
        for i in range(len(cost) - 2, -1, -1):
            dp[i] += min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])