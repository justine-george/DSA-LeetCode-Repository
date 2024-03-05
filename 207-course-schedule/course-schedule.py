class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = { crs: [] for crs in range(numCourses) }
        for crs, prereq in prerequisites:
            prereq_map[crs].append(prereq)

        seen_in_path = set()
        def dfs(crs):
            if prereq_map[crs] == []:
                return True
            if crs in seen_in_path:
                return False
            
            seen_in_path.add(crs)
            for prereq in prereq_map[crs]:
                if not dfs(prereq):
                    return False

            seen_in_path.remove(crs)
            prereq_map[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True