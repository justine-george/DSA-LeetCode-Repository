class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True
        cur.count += 1


    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for w in word:
            if w not in cur.children:
                return 0
            cur = cur.children[w]
        return cur.count if cur and cur.isWord else 0

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for w in prefix:
            if w not in cur.children:
                return 0
            cur = cur.children[w]
        
        # check all children's isWord and add
        st = [cur]
        res = 0
        while st:
            cur = st.pop()
            if cur.isWord:
                res += cur.count
            for child in cur.children.values():
                st.append(child)
        return res

    def erase(self, word: str) -> None:
        def erase_rec(node, word, i):
            if i == len(word):
                if node.isWord:
                    node.count -= 1
                    if node.count == 0:
                        node.isWord = False
                return node.count == 0 and len(node.children) == 0

            w = word[i]
            if w in node.children:
                if erase_rec(node.children[w], word, i + 1):
                    del node.children[w]
                    return not node.isWord and len(node.children) == 0
            return False

        erase_rec(self.root, word, 0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)