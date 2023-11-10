class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        for a, b in adjacentPairs:
            adj_map[a].append(b)
            adj_map[b].append(a)

        for key in adj_map:
            if len(adj_map[key]) == 1:
                start = key
                break
        
        stack = [start]
        visited = set()
        res = []
        while stack:
            n = stack.pop()
            res.append(n)
            visited.add(n)

            for neighbor in adj_map[n]:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return res