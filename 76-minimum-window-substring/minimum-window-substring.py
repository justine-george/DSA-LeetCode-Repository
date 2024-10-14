class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        t_count = Counter(t)
        window_count = Counter()
        
        matches = 0
        required = len(t_count)
        
        l = 0
        min_l, min_r = 0, float('inf')
        
        for r in range(len(s)):
            char = s[r]
            if char in t_count:
                window_count[char] += 1
                if window_count[char] == t_count[char]:
                    matches += 1
            
            while matches == required:
                if r - l < min_r - min_l:
                    min_l, min_r = l, r
                
                left_char = s[l]
                if left_char in t_count:
                    window_count[left_char] -= 1
                    if window_count[left_char] < t_count[left_char]:
                        matches -= 1
                l += 1
        
        return s[min_l:min_r+1] if min_r != float('inf') else ""