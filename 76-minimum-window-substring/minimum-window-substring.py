class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count_t, count_window = {}, {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t.keys())
        res, res_len = [-1, - 1], float('inf')

        l = 0
        for r in range(len(s)):
            c = s[r]

            count_window[c] = 1 + count_window.get(c, 0)

            if c in count_t and count_window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                
                # shrink from left
                c_left = s[l]
                count_window[c_left] -= 1
                if c_left in count_t and count_window[c_left] < count_t[c_left]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""