class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if r not in range(m) or c not in range(n) or board[r][c] != word[i] or (r, c) in visit:
                return False

            visit.add((r, c))
            
            res = False
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, i + 1):
                    res = True
                    break

            # res = (backtrack(r + 1, c, i + 1) or
            #     backtrack(r - 1, c, i + 1) or
            #     backtrack(r, c + 1, i + 1) or
            #     backtrack(r, c - 1, i + 1))

            visit.remove((r, c))

            return res
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False