class Solution:
    def betterCompression(self, compressed: str) -> str:
        map_arr = [0] * 26
        i = 0

        while i < len(compressed):
            char = compressed[i]
            i += 1

            start = i
            while i < len(compressed) and compressed[i].isdigit():
                i += 1

            map_arr[ord(char) - ord('a')] += int(compressed[start: i])
        
        # res = []
        # for i, count in enumerate(map_arr):
        #     if count > 0:
        #         res.append(chr(i + ord('a')))
        #         res.append(str(count))
        
        # return ''.join(res)
        return ''.join(f"{chr(i + ord('a'))}{str(count)}" for i, count in enumerate(map_arr) if count > 0)