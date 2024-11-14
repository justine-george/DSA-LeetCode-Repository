class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
    
    def prune(self, c):
        if c in self.children:
            del self.children[c]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = set()
        visit = set()

        root = TrieNode()
        for word in words:
            root.add(word)
        
        def dfs(r, c, cur_node, cur_word):
            if r < 0 or c < 0 or r == m or c == n or (r, c) in visit or board[r][c] not in cur_node.children:
                return
            
            cur_node = cur_node.children[board[r][c]]
            cur_word += board[r][c]

            if cur_node.is_word:
                res.add(cur_word)
                cur_node.is_word = False

            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, cur_node, cur_word)
            visit.remove((r, c))

            if not cur_node.children:
                cur_node.prune(board[r][c])

        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")

        return list(res)
        
