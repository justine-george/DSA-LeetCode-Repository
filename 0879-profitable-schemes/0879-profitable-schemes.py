class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # draw decision tree - backtracking
        # (n=total remaining, p=totalprofit, i=current index)
        #           (n=5, p=0, i=0) 
        #               /   \
        #              /     \
        # (n=3, p=2, i=1)    (n=5, p=0, i=1)
        #    chose i=0         didn't choose i=0
        
        
#         # T: O(n * m * p) -> m = length of group
#         # (i, m, p) -> number of ways we can generate profitable schemes with these params
#         dp = collections.defaultdict(int)
#         mod = 10**9 + 7
#         # setting base case
#         for m in range(n + 1):
#             dp[(len(group), m, minProfit)] = 1 # this is the case when i == len(group) in recursive solution
        
#         for i in range(len(group) -1, -1, -1): # iterate in reverse
#             for m in range(n + 1): # include n too
#                 for p in range(minProfit + 1): # include minProfit too
#                     dp[(i, m, p)] = dp[(i + 1, m, p)]
#                     if m + group[i] <= n:
#                         dp[(i, m, p)] += dp[(i + 1, m + group[i], min(minProfit, p + profit[i]))] % mod
        
#         return dp[(0, 0, 0)] % mod
    
        
        
        # backtracking with memoization - but time limit exceeded error on leetcode if min(minProfit, p + profit[i]) is not taken - reduce possible number of states
        # T: O(n * m * p) -> m = length of group
        mod = 10**9 + 7
        dp = {}
        def dfs(i, n, p):
            if i == len(group):
                return 1 if p >= minProfit else 0
            if (i, n, p) in dp:
                return dp[(i, n, p)]
            
            # skip the i
            dp[(i, n, p)] = dfs(i + 1, n, p)
            
            # or use i
            if n - group[i] >= 0:
                dp[(i, n, p)] += dfs(i + 1, n - group[i], min(minProfit, p + profit[i])) % mod
            
            return dp[(i, n, p)]
        
        return dfs(0, n, 0) % mod


#         # with @cache
#         # T: O(n * m * p) -> m = length of group
#         mod = 10**9 + 7
#         @cache
#         def dfs(i, n, p):
#             if i == len(group):
#                 return 1 if p >= minProfit else 0
#             # skip the i
#             skip = dfs(i + 1, n, p)
#             # or, pick i
#             pick = 0
#             if n - group[i] >= 0:
#                 pick = dfs(i + 1, n - group[i], min(minProfit, p + profit[i]))
            
#             return skip + pick
        
#         return dfs(0, n, 0) % mod