class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10,15,20]
        # [2  15 20  0]
        
        prevEndCost, endCost = cost[-1], 0
        for i in range(len(cost) - 2, -1, -1):
            newCost = cost[i] + min(prevEndCost, endCost)
            endCost = prevEndCost
            prevEndCost = newCost
        
        return min(prevEndCost, endCost)