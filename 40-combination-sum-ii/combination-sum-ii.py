class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        
        def backtrack(index, arr, total):
            if total == target:
                res.append(arr.copy())
                return
            
            for i in range(index, len(candidates)):
                # skip duplicates
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                # early stop since the array is sorted
                if candidates[i] + total > target:
                    break

                arr.append(candidates[i])
                backtrack(i + 1, arr, total + candidates[i])
                arr.pop()
            
        backtrack(0, [], 0)
        return res