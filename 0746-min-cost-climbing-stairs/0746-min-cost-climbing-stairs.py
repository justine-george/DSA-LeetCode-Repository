class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         # recursive solution
#         # T: O(n), S: O(n)
#         memo = {}
#         # @cache
#         # either use @cache or manually memoize
#         def dfs(i):
#             if i in memo:
#                 return memo[i]
#             if i <= 1:
#                 return 0
            
#             downOne = cost[i - 1] + dfs(i - 1)
#             downTwo = cost[i - 2] + dfs(i - 2)
            
#             memo[i] = min(downOne, downTwo)
#             return memo[i]
        
#         return dfs(len(cost))
    
        # iterative solution
        # solve from right to left
        # dp = cost.copy()
        # dp = dp + [0]
        # T: O(n), S: O(1)
        last = 0
        secondLast = cost[-1]
        for i in range(len(cost) - 2, -1, -1):
            # dp[i] = dp[i] + min(dp[i + 1], dp[i + 2])
            cur = cost[i] + min(secondLast, last)
            last = secondLast
            secondLast = cur
        return min(secondLast, last)
    
  #   10 15 20 0
  #       c  s  l
  #    c  s  l
  # c  s  l
  # finally min(s, l) is the result