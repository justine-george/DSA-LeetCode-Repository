class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        rowRange, colRange = set(range(0, m)), set(range(0, n))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r not in rowRange or c not in colRange or (r, c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True
            visited.remove((r, c))
            return False


        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False