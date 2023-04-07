class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = collections.defaultdict(lambda: 0)
        for c in s:
            sDict[c] += 1
        
        tDict = collections.defaultdict(lambda: 0)
        for c in t:
            tDict[c] += 1
        
        for c in s:
            if sDict[c] != tDict[c]:
                return False
        
        return True