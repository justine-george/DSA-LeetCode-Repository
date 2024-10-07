class Solution:
    def minJumps(self, arr: List[int]) -> int:
        same_val_indices_map = defaultdict(list)
        for i, a in enumerate(arr):
            same_val_indices_map[a].append(i)
        
        res = 0
        q = deque([0])
        visited = set([0])
        n = len(arr)
        while q:
            for _ in range(len(q)):
                cur_index = q.popleft()

                # Check if we've reached the last index
                if cur_index == n - 1:
                    return res
                
                # Check neighbours on the left and right
                neighbors = []
                if cur_index - 1 >= 0:
                    neighbors.append(cur_index - 1)
                if cur_index + 1 < n:
                    neighbors.append(cur_index + 1)

                # Add all indices with the same value as potential jumps
                # We only consider these neighbors once to avoid redundant traversals
                neighbors += same_val_indices_map[arr[cur_index]]

                # Clear the list to prevent future unnecessary check for these indices
                same_val_indices_map[arr[cur_index]].clear()
                
                # Visit all neighbors
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                
            res += 1
        
        return res