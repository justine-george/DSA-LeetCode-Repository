class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS
        q = deque([start])
        visited = set([start])
        while q:
            for _ in range(len(q)):
                st_index = q.popleft()
                if arr[st_index] == 0:
                    return True
                # jump to neighbors
                if st_index + arr[st_index] < len(arr) and st_index + arr[st_index] not in visited:
                    q.append(st_index + arr[st_index])
                    visited.add(st_index + arr[st_index])
                if st_index - arr[st_index] >= 0 and st_index - arr[st_index] not in visited:
                    q.append(st_index - arr[st_index])
                    visited.add(st_index - arr[st_index])
            
        return False