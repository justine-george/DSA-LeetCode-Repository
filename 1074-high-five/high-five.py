class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_marks_map = defaultdict(list)
        
        for id, score in items:
            heapq.heappush(id_marks_map[id], score)
            if len(id_marks_map[id]) > 5:
                heapq.heappop(id_marks_map[id])
        
        res = []
        for id in id_marks_map:
            avg = sum(id_marks_map[id])//len(id_marks_map[id])
            res.append([id, avg])
        
        self.sort_arr = res
        # return sorted(res, key=lambda x: x[0])
        return sorted(res, key=self.custom_comparator)
    
    def custom_comparator(self, n):
        return (n[0])