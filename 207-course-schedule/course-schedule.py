class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algorithm BFS with indegree tracking
        next_crs_map = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            next_crs_map[pre].append(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res_len = 0
        while q:
            crs = q.popleft()
            res_len += 1

            for next_crs in next_crs_map[crs]:
                indegree[next_crs] -= 1
                if indegree[next_crs] == 0:
                    q.append(next_crs)

        return True if res_len == numCourses else False

        # next_crs_map = {i: [] for i in range(numCourses)}

        # for crs, pre in prerequisites:
        #     next_crs_map[pre].append(crs)
        
        # # {crs: True (in current path) | False (visited) | no key (not visited)}
        # visit = {}
        # # post order dfs, topological sort
        # def dfs(i):
        #     if i in visit:
        #         return visit[i]

        #     visit[i] = True
        #     for next_crs in next_crs_map[i]:
        #         if dfs(next_crs):
        #             return True

        #     visit[i] = False
        #     return False

        # for crs in next_crs_map:
        #     if dfs(crs):
        #         return False

        # return True