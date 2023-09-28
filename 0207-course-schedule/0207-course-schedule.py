class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree list - depends on count
        indegree = [0] * numCourses
        # form the adjacency list, [x serves y]
        adj_list = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
            indegree[crs] += 1
        
        queue = deque()
        # add those with indegree 0 to the queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            pre = queue.popleft()
            res.append(pre)
            for crs in adj_list[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    queue.append(crs)

        # if we can visit all, then all courses can be finished
        return len(res) == numCourses