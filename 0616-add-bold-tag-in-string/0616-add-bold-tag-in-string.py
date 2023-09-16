class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
#         <b>a<b>a</b>a</b><b>b</b><b>b</b><b>b</b>
        
#         <b>aaabbb</b>
        
        isCharBold = [False] * len(s)
        
        for word in words:
            start = s.find(word)
            length = len(word)
            
            while start != -1:
                for i in range(start, start + length):
                    isCharBold[i] = True
                
                start = s.find(word, start + 1)
            
        res = ""
        # isFirstBold = True
        isBolding = False
        for i, val in enumerate(isCharBold):
            if val:
                if not isBolding:
                    isBolding = True
                    res += '<b>'
                res += s[i]
            else:
                if isBolding:
                    isBolding = False
                    res += '</b>'
                res += s[i]
        if isBolding:
            res += '</b>'
        return res
                