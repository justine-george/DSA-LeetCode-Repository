class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        # return parent
        def find(node):
            node = parent[node]
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        # combine
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 != par2:
                if rank[par1] > rank[par2]:
                    parent[par2] = par1
                    rank[par1] += 1
                else:
                    parent[par1] = par2
                    rank[par2] += 1
                return 1
            else:
                return 0

        res = n
        for u, v in edges:
            res -= union(u, v)

        return res
