class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isPermutation(s1, s2):
            if len(s1) != len(s2):
                return False
            
            counts1 = {}
            counts2 = {}
            for i in range(len(s1)):
                counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
                counts2[s2[i]] = 1 + counts2.get(s2[i], 0)
            
            return counts1 == counts2
        
        l = 0 
        for r in range(len(s1) - 1, len(s2)):
            if isPermutation(s2[l:r + 1], s1):
                return True
            l += 1
        return False