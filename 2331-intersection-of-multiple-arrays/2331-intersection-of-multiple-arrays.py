class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count_map = {}
        
        for i, list in enumerate(nums):
            for j, num in enumerate(list):
                count_map[num] = 1 + count_map.get(num, 0)
                    
        res = []
        for num, count in count_map.items():
            if count == len(nums):
                res.append(num)
                
        return sorted(res)