class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # max_in_path, x, y
        min_heap = [(grid[0][0], 0, 0)]
        dim = len(grid)
        visit = set([(0, 0)])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while min_heap:
            max_in_path, x, y = heapq.heappop(min_heap)
            visit.add((x, y))

            if x == dim - 1 and y == dim - 1:
                return max_in_path
            
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x in range(dim) and new_y in range(dim) and (new_x, new_y) not in visit:
                    heapq.heappush(min_heap, (max(max_in_path, grid[new_x][new_y]), new_x, new_y))
                    visit.add((new_x, new_y))