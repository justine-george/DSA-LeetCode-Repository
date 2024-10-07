class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS
        q = deque([start])
        visited = set([start])
        while q:
            st_index = q.popleft()
            if arr[st_index] == 0:
                return True
            # jump to neighbors
            for next_index in [st_index + arr[st_index], st_index - arr[st_index]]:
                if 0 <= next_index < len(arr) and next_index not in visited:
                    q.append(next_index)
                    visited.add(next_index)
            
        return False