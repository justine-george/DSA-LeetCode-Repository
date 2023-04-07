class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # sDict = collections.defaultdict(lambda: 0)
        sDict = {}
        for c in s:
            # sDict[c] += 1
            sDict[c] = 1 + sDict.get(c, 0)

        # tDict = collections.defaultdict(lambda: 0)
        tDict = {}
        for c in t:
            # tDict[c] += 1
            tDict[c] = 1 + tDict.get(c, 0)
        
        for c in s:
            if sDict[c] != tDict.get(c, -1):
                return False
        
        return True