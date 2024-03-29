class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]] # path compression
                res = parent[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0 # means union failed
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1 # means union is success
        res = n
        for n1, n2 in edges:
            # decrement count of isolated components if union is successful
            res -= union(n1, n2)
        return res
        