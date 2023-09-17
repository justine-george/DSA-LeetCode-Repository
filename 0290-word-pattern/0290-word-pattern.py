class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        mapCharToWord = {}
        mapWordToChar = {}
        
        if len(pattern) != len(words):
            return False
        
        for i, c in enumerate(pattern):
            if c not in mapCharToWord:
                mapCharToWord[c] = words[i]
            else:
                if mapCharToWord[c] != words[i]:
                    return False
            
            if words[i] not in mapWordToChar:
                mapWordToChar[words[i]] = c
            else:
                if mapWordToChar[words[i]] != c:
                    return False
        
        return True