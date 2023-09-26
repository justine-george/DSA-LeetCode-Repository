class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # different approach, kahn's algorithm
        # [[1,4],[2,4],[3,1],[3,2]]

        # adj
        # [[],[3],[3],[],[1, 2]]

        # indegree
        # [0,0,0,0,0]

        # queue = []

        # visited = 5
        
        # node = 3

        indegree = [0] * numCourses
        # pre: course mapping
        map = [[] for _ in range(numCourses)]
        for c, pre in prerequisites:
            map[pre].append(c)
            indegree[c] += 1

        queue = deque()
        for i, c in enumerate(indegree):
            if c == 0:
                queue.append(i)

        visitedCount = 0
        while queue:
            crs = queue.popleft()
            visitedCount += 1
            
            for c in map[crs]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
        
        return visitedCount == numCourses

        # def dfs(crs):
        #     if crs in visited:
        #         return False
            
        #     if map[crs] == []:
        #         return True
            
        #     visited.add(crs)
        #     for pre in map[crs]:
        #         if not dfs(pre):
        #             return False
        #     visited.remove(crs)
        #     map[crs] = []
        #     return True
        
        # map = {i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     map[crs].append(pre)

        # visited = set()

        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        
        # return True