class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        rows, cols = set(range(m)), set(range(n))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def does_word_exist(r, c, i):
            if i == len(word):
                return True

            if r not in rows or c not in cols or (r, c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if does_word_exist(nr, nc, i + 1):
                    return True

            visited.remove((r, c))
            return False


        for r in range(m):
            for c in range(n):
                if does_word_exist(r, c, 0):
                    return True
        return False