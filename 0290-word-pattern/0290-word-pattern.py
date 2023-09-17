class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        mapCharToWord = {}
        mapWordToChar = {}
        for c, word in zip(pattern, words):
            if c in mapCharToWord and mapCharToWord[c] != word:
                return False
            if word in mapWordToChar and mapWordToChar[word] != c:
                return False
            
            mapCharToWord[c] = word
            mapWordToChar[word] = c
            
        return True