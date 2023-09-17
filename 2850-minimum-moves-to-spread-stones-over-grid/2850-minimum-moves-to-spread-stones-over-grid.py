class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        dist = lambda x,y: abs(x[0]-y[0])+ abs(x[1]-y[1])  
        zeros, extras = [], []

        for i,j in product(range(3),range(3)):
            stone = grid[i][j]
            if stone == 0: zeros.append((i,j))
            if stone  > 1: extras.extend([(i,j)]*(stone-1))

        return min((sum(map(dist, zeros, per))) for per in set(permutations(extras)))
        
#         1 3 0
#         1 0 0
#         1 0 3
        
#         zeros: [(0, 2), (1, 1), (1, 2), (2, 1)]
#         extras: [(0, 1), (0, 1), (2, 2), (2, 2)]
        
        # {
        #     ((2, 2), (0, 1), (0, 1),(2, 2)),
        #     ((2, 2), (2, 2), (0, 1), (0, 1)),
        #     ((0, 1), (2, 2), (0, 1), (2, 2)),
        #     ((0, 1), (0, 1), (2, 2), (2, 2)),
        #     ((0, 1), (2, 2), (2, 2), (0, 1)),
        #     ((2, 2), (0, 1), (2, 2), (0, 1))
        # }