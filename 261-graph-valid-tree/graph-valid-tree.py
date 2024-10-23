class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        parent = [i for i in range(n)]
        rank = [1] * n

        def find_parent(node):
            node = parent[node]
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(node1, node2):
            par1, par2 = find_parent(node1), find_parent(node2)
            if par1 == par2:
                return False
            else:
                if rank[par1] > rank[par2]:
                    rank[par1] += 1
                    parent[par2] = par1
                else:
                    rank[par2] += 1
                    parent[par1] = par2
                return True
        
        res = n
        for u, v in edges:
            if not union(u, v):
                return False
            res -= 1
        return res == 1