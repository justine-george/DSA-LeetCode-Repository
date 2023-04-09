class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}
        # @cache
        def dfs(i):
            if i in memo:
                return memo[i]
            if i <= 1:
                return 0
            
            downOne = cost[i - 1] + dfs(i - 1)
            downTwo = cost[i - 2] + dfs(i - 2)
            
            memo[i] = min(downOne, downTwo)
            return memo[i]
        
        return dfs(len(cost))