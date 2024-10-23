class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # {char: set()}
        next_char_map = {c: set() for w in words for c in w}

        for i in range(1, len(words)):
            prevWord, word = words[i - 1], words[i]
            minLen = min(len(prevWord), len(word))
            
            if prevWord[:minLen] == word[:minLen] and len(prevWord) > len(word):
                return ""
            
            for i in range(minLen):
                if prevWord[i] != word[i]:
                    next_char_map[prevWord[i]].add(word[i])
                    break

        
        # post-order dfs, topological sort
        visit = {} # { char: False (is visited) | True (in current path) | no key means not visited}

        # add children, then first, so at the end, return in reverse
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for next_char in next_char_map[c]:
                if dfs(next_char): # cycle detected
                    return True
            
            res.append(c)
            visit[c] = False

        for c in next_char_map:
            if dfs(c): # cycle detected
                return ""
        
        res.reverse()
        return "".join(res)