class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, newWord):
        cur = self
        for c in newWord:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
    def prune(self, c):
        if c in self.children:
            del self.children[c]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        path = set()
        m, n = len(board), len(board[0])
        valid_rows, valid_cols = set(range(m)), set(range(n))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = set()
        
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        # word starts with "" and tracks full word
        def backtrack(r, c, node, curWord):
            if r not in valid_rows or c not in valid_cols or board[r][c] not in node.children or (r, c) in path:
                return
            
            curChar = board[r][c]
            curWord.append(curChar)
            cur = node.children[curChar]

            if cur.isWord:
                res.add("".join(curWord))
                cur.isWord = False

            path.add((r, c))
            for dr, dc in directions:
                backtrack(r + dr, c + dc, cur, curWord)
            path.remove((r, c))
            curWord.pop()

            if not cur.children:
                node.prune(curChar)

        for i in range(m):
            for j in range(n):
                backtrack(i, j, root, [])

        return list(res)