class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # using DFS
        def dfs(crs):
            if crs in current_path:
                return False

            if crs in visited:
                return True

            current_path.add(crs)

            for pre in map[crs]:
                if not dfs(pre):
                    return False
            
            visited.add(crs)
            current_path.remove(crs)
            
            res.append(crs)
            return True

        res = []

        # keep track of current visited
        current_path = set()

        # keep track of ones completely traversed
        visited = set()

        # build an adjacency list
        map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            map[crs].append(pre)
        
        for c in range(numCourses):
            if c not in visited and not dfs(c):
                return []

        return res

        # # kahn's algorithm using adj_list, preq_count_list and a deque
        # res = []
        # depends_on_count = [0] * numCourses
        # adj_list = [[] for i in range(numCourses)]
        # for crs, pre in prerequisites:
        #     adj_list[pre].append(crs)
        #     depends_on_count[crs] += 1
        
        # queue = deque()
        # for c in range(numCourses):
        #     if depends_on_count[c] == 0:
        #         queue.append(c)

        # visited_count = 0
        # while queue:
        #     crs = queue.popleft()
        #     visited_count += 1
        #     res.append(crs)

        #     for dependent in adj_list[crs]:
        #         depends_on_count[dependent] -= 1
        #         if depends_on_count[dependent] == 0:
        #             queue.append(dependent)
        
        # return res if visited_count == numCourses else []