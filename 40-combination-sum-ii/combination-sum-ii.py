class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        candidates.sort()
        res = []
        
        def backtrack(index, arr, total):
            if total == target:
                res.append(arr)
                return
            
            for i in range(index, n):
                # skip duplicates
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] + total > target:
                    break
            
                backtrack(i + 1, arr + [candidates[i]], total + candidates[i])
            
        backtrack(0, [], 0)
        return res