class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # T: O(n^2), S: O(n^2)
        dp = {}
        def dfs(i, remain):
            if remain <= 0:
                return 0
            if i == len(cost):
                return float("inf")
            
            if (i, remain) in dp:
                return dp[(i, remain)]

            # paint the wall
            paint = cost[i] + dfs(i + 1, remain - 1 - time[i])
            # skip
            skip = dfs(i + 1, remain)

            dp[(i, remain)] = min(paint, skip)
            return dp[(i, remain)]
        
        return dfs(0, len(cost))