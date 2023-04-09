class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dict = {(m-1, n-1): 0}
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    dict[(i, j)] = 1
                else:
                    dict[(i, j)] = dict[(i + 1, j)] + dict[(i, j + 1)]
        
        return dict[(0, 0)]