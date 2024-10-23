class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        next_map = {i: set() for i in range(numCourses)}

        for crs, pre in prerequisites:
            next_map[pre].add(crs)
        
        # {i: False (visited) | True (in the current path) | no key (not visited)}
        visit = {}

        # post-order dfs, topological sort
        def dfs(i):
            if i in visit:
                return visit[i]
            
            visit[i] = True
            for next_crs in next_map[i]:
                if dfs(next_crs): # cycle detected
                    return True
            res.append(i)
            visit[i] = False

        res = []
        for i in next_map:
            if dfs(i): # cycle detected
                return []
        
        res.reverse()
        return res