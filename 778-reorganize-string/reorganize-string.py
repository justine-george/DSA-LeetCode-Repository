class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the frequency of each character
        char_counts = Counter(s)
        # Create a max heap from char counts
        max_heap = [(-cnt, char) for char, cnt in char_counts.items()]
        heapq.heapify(max_heap)

        result = []
        # Keep track of the last character added to the result to avoid consecutive duplicates
        prev_cnt, prev_char = 0, ''
        
        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            # Add the current character to the result
            result.append(char)
            # Since we are using a max heap, we add 1 (because counts are negative)
            if prev_cnt < 0:
                # If there's a previous character to add back, do it now
                heapq.heappush(max_heap, (prev_cnt, prev_char))
            
            # Update prev_char and decrease its count for the next round
            prev_cnt, prev_char = cnt + 1, char
        
        # If the last character count is less than 0, we couldn't reorganize successfully
        return ''.join(result) if len(result) == len(s) else ""