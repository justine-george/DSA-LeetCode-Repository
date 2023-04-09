class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def dfs(i):
            if i <= 1:
                return 0
            
            downOne = cost[i - 1] + dfs(i - 1)
            downTwo = cost[i - 2] + dfs(i - 2)
            
            return min(downOne, downTwo)
        
        return dfs(len(cost))