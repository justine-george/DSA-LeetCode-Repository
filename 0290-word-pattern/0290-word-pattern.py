class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        mapCharToWord = {}
        mapWordToChar = {}
        for c, word in zip(pattern, words):
            if c not in mapCharToWord:
                mapCharToWord[c] = word
            else:
                if mapCharToWord[c] != word:
                    return False
            
            if word not in mapWordToChar:
                mapWordToChar[word] = c
            else:
                if mapWordToChar[word] != c:
                    return False
        
        return True