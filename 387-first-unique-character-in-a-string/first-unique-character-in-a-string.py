class Solution:
    def firstUniqChar(self, s: str) -> int:
        # char: [latest_index, freq]
        map = {}
        for i, c in enumerate(s):
            if c not in map:
                map[c] = [i, 0]
            map[c] = [i, map[c][1] + 1]
        
        for char, [latest_index, freq] in map.items():
            if freq == 1:
                return latest_index

        return -1
