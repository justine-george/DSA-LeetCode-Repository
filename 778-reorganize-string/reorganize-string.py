class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)

        prev_count, prev_char = 0, ''
        res = ""

        while max_heap:
            count, char = heapq.heappop(max_heap)
            res += char

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            prev_count, prev_char = count + 1, char

        
        return res if len(res) == len(s) else ""
