class Solution:
    def clearStars(self, s: str) -> str:
        # T: O(nlogn), S: O(n) (storing indeces of s in each of the 26 keys)
        count_map = {chr(i): [] for i in range(ord('a'), ord('z') + 1)}
        # top shows current smallest character
        min_heap = []
        heapq.heapify(min_heap)
        
        temp_s = []
        
        for i, c in enumerate(s):
            if c != '*':
                if len(count_map[c]) == 0:
                    heapq.heappush(min_heap, ord(c))
                
                # append its index to the end of value list
                count_map[c].append(i)
                
                temp_s.append(c)
                
            else:
                smallest_c_left = chr(min_heap[0])
                del_index = count_map[smallest_c_left][-1]
                
                # mark as delete
                temp_s[del_index] = '*'
                
                # delete this index
                count_map[smallest_c_left].pop()
                
                if len(count_map[smallest_c_left]) == 0:
                    heapq.heappop(min_heap)
                
                temp_s.append('*')

        # form final string and return
        return "".join(c for c in temp_s if c != '*')