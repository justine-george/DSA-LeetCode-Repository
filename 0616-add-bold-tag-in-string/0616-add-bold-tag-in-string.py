class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:      
        isCharBold = [False] * len(s)
        
        # mask all characters to be emboldened
        for word in words:
            start = s.find(word)
            length = len(word)
            
            while start != -1:
                for i in range(start, start + length):
                    isCharBold[i] = True
                start = s.find(word, start + 1)
            
        res = ""
        isBolding = False
        for i, val in enumerate(isCharBold):
            if val:
                if not isBolding:
                    isBolding = True
                    res += '<b>'
            else:
                if isBolding:
                    isBolding = False
                    res += '</b>'
            res += s[i]
            
        # edge case when last character is marked to be emboldened
        if isBolding:
            res += '</b>'
            
        return res