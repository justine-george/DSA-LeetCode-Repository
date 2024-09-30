class Solution:
    def betterCompression(self, compressed: str) -> str:
        map_arr = [0] * 26
        i = 0

        while i < len(compressed):
            char = compressed[i]
            i += 1

            count = ''
            while i < len(compressed) and '0' <= compressed[i] <= '9':
                count += compressed[i]
                i += 1

            map_arr[ord(char) - ord('a')] += int(count)
        
        res = []
        for i, count in enumerate(map_arr):
            if count > 0:
                res.append(chr(i + ord('a')))
                res.append(str(count))
        
        return ''.join(res)
