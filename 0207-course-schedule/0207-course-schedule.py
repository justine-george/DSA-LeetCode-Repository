class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(crs):
            if crs in visit_set:
                return False
            
            if pre_map[crs] == []:
                return True
            
            visit_set.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            visit_set.remove(crs)
            pre_map[crs] = []
            return True
        
        # adjacency list
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # visit set = all courses along the curr DFS path
        visit_set = set()

        # check whether each course is doable
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True