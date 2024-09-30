class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = defaultdict(int)
        for c in s:
            freq_map[c] += 1
        
        for i, c in enumerate(s):
            if freq_map[c] == 1:
                return i

        return -1
