class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological ordering
        prereq_map = collections.defaultdict(list)
        for crs, prereq in prerequisites:
            prereq_map[crs].append(prereq)

        unvisited = set(range(numCourses))
        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)

            # iterate over prereqs
            for prereq in prereq_map[crs]:
                if not dfs(prereq):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            return True

        while unvisited:
            crs = unvisited.pop()

            if crs in visited:
                continue
            
            if not dfs(crs):
                return False
        
        return True
