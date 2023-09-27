class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        depends_on_count = [0] * numCourses
        adj_list = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
            depends_on_count[crs] += 1
        
        queue = deque()
        for c in range(numCourses):
            if depends_on_count[c] == 0:
                queue.append(c)

        visited_count = 0
        while queue:
            crs = queue.popleft()
            visited_count += 1
            res.append(crs)

            for dependent in adj_list[crs]:
                depends_on_count[dependent] -= 1
                if depends_on_count[dependent] == 0:
                    queue.append(dependent)
        
        return res if visited_count == numCourses else []