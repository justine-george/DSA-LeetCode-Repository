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
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.count -= 1
        if cur.count == 0:
            cur.isWord = False
        # cur.children = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)