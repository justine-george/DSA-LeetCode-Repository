class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4:
            return False
        matchsticks.sort(reverse=True)
        
        targetLength = sum(matchsticks) / 4
        used = [False] * len(matchsticks);
        
        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            
            if targetLength == subsetSum:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(matchsticks)):
                if used[j] or subsetSum + matchsticks[j] > targetLength:
                    continue
                
                used[j] = True
                if backtrack(j + 1, k, subsetSum + matchsticks[j]):
                    return True
                used[j] = False
                
            return False
        
        return backtrack(0, 4, 0)
        