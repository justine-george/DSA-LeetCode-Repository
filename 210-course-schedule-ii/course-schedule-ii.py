class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Both approaches have same time and space complexity
        # T: O(n), S: O(n)

        # next_map = {i: set() for i in range(numCourses)}

        # for crs, pre in prerequisites:
        #     next_map[pre].add(crs)
        
        # # {i: False (visited) | True (in the current path) | no key (not visited)}
        # visit = {}

        # # post-order dfs, topological sort
        # def dfs(i):
        #     if i in visit:
        #         return visit[i]
            
        #     visit[i] = True
        #     for next_crs in next_map[i]:
        #         if dfs(next_crs): # cycle detected
        #             return True
        #     res.append(i)
        #     visit[i] = False

        # res = []
        # for i in next_map:
        #     if dfs(i): # cycle detected
        #         return []
        
        # res.reverse()
        # return res

        next_map = {i: set() for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            next_map[pre].add(crs)
            indegree[crs] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)

            for next_crs in next_map[crs]:
                indegree[next_crs] -= 1
                if indegree[next_crs] == 0:
                    q.append(next_crs)

        return res if len(res) == numCourses else []