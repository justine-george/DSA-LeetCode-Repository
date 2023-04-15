class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # similar to 567. Permutation in String, sliding window
        res = []
        if len(p) > len(s):
            return res
        
        pcount, scount = collections.defaultdict(lambda: 0), collections.defaultdict(lambda: 0)
        
        for i in range(len(p)):
            pcount[p[i]] += 1
            scount[s[i]] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if pcount[chr(i + ord('a'))] == scount[chr(i + ord('a'))] else 0)
            
        l = 0
        for r in range(len(p), len(s)):
            if matches == 26:
                res.append(l)
            
            # current char is s[r]
            scount[s[r]] += 1
            if scount[s[r]] == pcount[s[r]]: # now equal
                matches += 1
            elif scount[s[r]] - 1 == pcount[s[r]]: # were equal
                matches -= 1
            
            # char to be removed from window is s[l]
            scount[s[l]] -= 1
            if scount[s[l]] == pcount[s[l]]: # now equal
                matches += 1
            elif scount[s[l]] + 1 == pcount[s[l]]: # were equal
                matches -= 1
            l += 1
        
        if matches == 26:
            res.append(l)
        return res