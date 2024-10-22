class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # how much extra to send each of them to city_a
        diff = [(cost_a - cost_b, cost_a, cost_b) for cost_a, cost_b in costs]
        diff.sort()
    
        total_cost = 0
        for i in range(len(diff)):
            if i < len(diff) // 2:
                total_cost += diff[i][1]
            else:
                total_cost += diff[i][2]
        return total_cost