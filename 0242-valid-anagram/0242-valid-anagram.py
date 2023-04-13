class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False
        
        # sDict, tDict = collections.defaultdict(lambda:0), collections.defaultdict(lambda:0)
        sDict, tDict = {}, {}
        for i in range(len(s)):
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)
            # sDict[s[i]] += 1 #+ sDict.get(s[i], 0)
            # tDict[t[i]] += 1 #+ tDict.get(t[i], 0)
        
        for c in sDict:
            if sDict[c] != tDict.get(c, -1):
            # if sDict[c] != tDict[c]:
                return False            
        
        return True