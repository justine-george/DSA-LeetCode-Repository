class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = r = 0
        freq_map = [0] * 26
        max_freq = 0
        max_len = 0
        while l <= r and r < len(s):
            freq_map[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, freq_map[ord(s[r]) - ord('A')])
            while l <= r and (r - l + 1) - max_freq > k:
                freq_map[ord(s[l]) - ord('A')] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len