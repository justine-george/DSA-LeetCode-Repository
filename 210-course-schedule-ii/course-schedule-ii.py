class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = { crs: [] for crs in range(numCourses) }
        for crs, prereq in prerequisites:
            prereq_map[crs].append(prereq)
        
        # unvisited nodes
        white = set([crs for crs in range(numCourses)])
        # presently in the cycle
        grey = set()
        # visited completely
        black = set()

        def dfs(crs):
            if crs in black:
                return True
            
            if crs in grey:
                return False
            
            grey.add(crs)

            for prereq in prereq_map[crs]:
                if not dfs(prereq):
                    return False
            
            black.add(crs)
            order.append(crs)
            grey.remove(crs)
            return True


        order = []
        while white:
            crs = white.pop()

            if crs in black:
                continue
            
            if not dfs(crs):
                return []
        
        return order