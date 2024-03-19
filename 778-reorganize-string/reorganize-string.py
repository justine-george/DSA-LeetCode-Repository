class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev_cnt, prev_char = 0, ''
        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            res += char

            if prev_cnt < 0:
                heapq.heappush(maxHeap, [prev_cnt, prev_char])

            prev_cnt, prev_char = cnt + 1, char
        
        return res if len(res) == len(s) else ""