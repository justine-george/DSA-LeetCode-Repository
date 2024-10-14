class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq_map = Counter(t)
        window_freq_map = Counter()

        l = 0
        min_l, min_r = 0, float('inf')
        have, need = 0, len(t_freq_map)
        
        for r in range(len(s)):
            r_char = s[r]
            window_freq_map[r_char] += 1
            if r_char in t_freq_map and window_freq_map[r_char] == t_freq_map[r_char]:
                have += 1
            
            while have == need:
                if r - l < min_r - min_l:
                    min_l, min_r = l, r
                
                l_char = s[l]
                window_freq_map[l_char] -= 1
                if l_char in t_freq_map and window_freq_map[l_char] < t_freq_map[l_char]:
                    have -= 1
                l += 1
        
        return s[min_l:min_r + 1] if min_r != float('inf') else ""