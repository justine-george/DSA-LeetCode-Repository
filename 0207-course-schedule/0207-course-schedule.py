class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # using DFS
        def dfs(crs):
            if crs in cycle_set:
                return False
            
            if crs in visited_set:
                return True

            cycle_set.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            cycle_set.remove(crs)

            visited_set.add(crs)
            return True
        
        adj_list = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        # 2 sets
        visited_set, cycle_set = set(), set() 

        # for each course, if cycle exists, return False
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        # # different approach, kahn's algorithm
        # # [[1,4],[2,4],[3,1],[3,2]]

        # # adj
        # # [[],[3],[3],[],[1, 2]]

        # # indegree
        # # [0,0,0,0,0]

        # # queue = []

        # # visited = 5
        
        # # node = 3

        # indegree = [0] * numCourses
        # # pre: course mapping
        # map = [[] for _ in range(numCourses)]
        # for c, pre in prerequisites:
        #     map[pre].append(c)
        #     indegree[c] += 1

        # queue = deque()
        # for i, c in enumerate(indegree):
        #     if c == 0:
        #         queue.append(i)

        # visitedCount = 0
        # while queue:
        #     crs = queue.popleft()
        #     visitedCount += 1
            
        #     for c in map[crs]:
        #         indegree[c] -= 1
        #         if indegree[c] == 0:
        #             queue.append(c)
        
        # return visitedCount == numCourses