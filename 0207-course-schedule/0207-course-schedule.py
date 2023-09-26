class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(crs):
            if crs in visited:
                return False

            if map[crs] == []:
                return True
            
            visited.add(crs)
            for pre in map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            map[crs] = []
            return True

        # build adjacency list
        map = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            map[c].append(p)

        # keep track of visited in current DFS
        visited = set()

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True