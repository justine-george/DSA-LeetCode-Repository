class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_marks_map = defaultdict(list)
        
        for item in items:
            id, score = item
            if len(id_marks_map[id]) < 5:
                heapq.heappush(id_marks_map[id], score)
            elif score > id_marks_map[id][0]:
                heapq.heappop(id_marks_map[id])
                heapq.heappush(id_marks_map[id], score)
        
        res = []
        for id in id_marks_map.keys():
            total = 0
            while id_marks_map[id]:
                total += heapq.heappop(id_marks_map[id])
            avg = total // 5
            res.append([id, avg])
        
        return sorted(res)