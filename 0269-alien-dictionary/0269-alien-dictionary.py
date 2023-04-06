class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            minLen = min(len(w1), len(w2))
            
            # invalid order
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        visited = {}
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            
            for neighbor in adj[c]:
                if dfs(neighbor): # cycle detected
                    return True
            
            # post order dfs
            visited[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c): # cycle detected
                return ""
        
        # reversedWord = res[::-1] # reverse list
        res.reverse()
        
        return "".join(res) # [a, b, c] to abc