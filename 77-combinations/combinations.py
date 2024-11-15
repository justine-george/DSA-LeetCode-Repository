class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(start, level):
            if level == k:
                res.append(path[:])
                return
            
            for j in range(start, n + 1):
                path.append(j)
                backtrack(j + 1, level + 1)
                path.pop()
        
        backtrack(1, 0)
        return res