class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        rows, cols = set(range(m)), set(range(n))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []

        def dfs(r, c, node, word):
            if r not in rows or c not in cols or board[r][c] not in node.children:
                return
            
            curChar = board[r][c]
            parent = node
            node = node.children[curChar]
            word += curChar
            if node.isWord:
                res.append(word)
                node.isWord = False
                if not node.children:
                    # del parent.children[curChar]
                    del node
                    return

            board[r][c] = '.' # mark as visited
            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)
            board[r][c] = curChar # restore
        
        
        root = Trie()
        for word in words:
            root.addWord(word)

        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")
        
        return res