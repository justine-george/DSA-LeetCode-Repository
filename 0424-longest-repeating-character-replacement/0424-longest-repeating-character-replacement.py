class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freq_map = {}
        max_freq = 0
        max_len = 0
        while r < len(s):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(max_freq, freq_map[s[r]])
            while l <= r and (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len