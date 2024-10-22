class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # DP solution: T: O(n^2), S: O(n^2)
        cache = {}
        def dfs(i, k1, k2):
            if (k1, k2) in cache:
                return cache[(k1, k2)]
            
            if i == len(costs):
                return 0
            
            l = float('inf')
            r = float('inf')

            if k1 > 0:
                l = costs[i][0] + dfs(i + 1, k1 - 1, k2)
            if k2 > 0:
                r = costs[i][1] + dfs(i + 1, k1, k2 - 1)
            
            cache[(k1, k2)] = min(l, r)
            return cache[(k1, k2)]
        
        return dfs(0, len(costs) // 2, len(costs) // 2)

        # # Greedy solution, T: O(nlogn), S: O(n)
        # # how much extra to send each of them to city_a
        # diff = [(cost_a - cost_b, cost_a, cost_b) for cost_a, cost_b in costs]
        # diff.sort()
    
        # total_cost = 0
        # for i in range(len(diff)):
        #     if i < len(diff) // 2:
        #         total_cost += diff[i][1]
        #     else:
        #         total_cost += diff[i][2]
        # return total_cost