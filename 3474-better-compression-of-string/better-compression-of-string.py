class Solution:
    def betterCompression(self, compressed: str) -> str:
        map = defaultdict(int)
        i = 0
        while i < len(compressed):
            char = compressed[i]
            i += 1

            count = ''
            while i < len(compressed) and '0' <= compressed[i] <= '9':
                count += compressed[i]
                i += 1
            i -= 1

            map[char] += int(count)
            i += 1
        
        res = []
        for char, count in sorted(map.items()):
            res.append(char)
            res.append(str(count))
        
        return ''.join(res)
