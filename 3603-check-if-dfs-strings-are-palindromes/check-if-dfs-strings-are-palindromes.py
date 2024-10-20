class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        child = defaultdict(list)
        root = -1
        for i, p in enumerate(parent):
            if p == -1:
                root = i
            else:
                child[p].append(i)
        
        order = []
        n = len(parent)
        res = [False] * n
        
        def dfs(cur):
            tmp = ''
            for c in child[cur]:
                tmp += dfs(c)
            tmp += s[cur]
            res[cur] = tmp == tmp[::-1]
            return tmp
        
        dfs(root)
        return res