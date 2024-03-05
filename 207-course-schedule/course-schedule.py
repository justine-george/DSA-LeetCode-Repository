class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
        # [0, 1] means do 1 then 0
        # 0: 1, 2 ie. 1 and 2 are prereqs of 0
        # 1: 3, 4
        # 2: 
        # 3: 4
        # 4: 
        # prereq_map = collections.defaultdict(list)
        prereq_map = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # stores courses along the curr DFS path
        visitSet = set()
        def dfs(course):
            if prereq_map[course] == []:
                return True
            if course in visitSet:
                return False
            
            visitSet.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            visitSet.remove(course)
            prereq_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        