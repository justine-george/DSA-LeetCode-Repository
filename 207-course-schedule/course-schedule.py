class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        next_crs_map = {i: set() for i in range(numCourses)}

        for crs, pre in prerequisites:
            next_crs_map[pre].add(crs)
        
        # {crs: True (in current path) | False (visited) | no key (not visited)}
        visit = {}
        # post order dfs, topological sort
        def dfs(i):
            if i in visit:
                return visit[i]

            visit[i] = True
            for next_crs in next_crs_map[i]:
                if dfs(next_crs):
                    return True

            visit[i] = False
            return False

        for crs in next_crs_map:
            if dfs(crs):
                return False

        return True
