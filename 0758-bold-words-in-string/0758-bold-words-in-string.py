class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        isCharBold = [False] * len(s)
        
        for word in words:
            start = s.find(word)
            length = len(word)
            
            while start != -1:
                for i in range(start, start + length):
                    isCharBold[i] = True
                
                start = s.find(word, start + 1)
            
        res = ""
        # isInProgress = False
        i = 0
        while i < len(s):
            while i < len(s) and not isCharBold[i]:
                res += s[i]
                i += 1
            
            if i == len(s):
                break
            
            res += '<b>'
            while i < len(s) and isCharBold[i]:
                res += s[i]
                i += 1
            res += '</b>'

        return res