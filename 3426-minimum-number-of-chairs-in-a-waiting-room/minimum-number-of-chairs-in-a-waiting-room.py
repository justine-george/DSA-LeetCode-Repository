class Solution:
    def minimumChairs(self, s: str) -> int:
        cap, occ = 0, 0
        
        for c in s:
            if c == 'E':
                occ += 1
            else:
                occ -= 1
            cap = max(cap, occ)
        
        return cap