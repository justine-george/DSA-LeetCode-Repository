class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # res = []
        
        # minLen = 1001
        # compareindex = -1
        # for i, list in enumerate(nums):
        #     if len(list) < minLen:
        #         minLen = len(list)
        #         compareindex = i
        
        # for n in nums[compareindex]:
        #     # go through every array in nums
        #     present = True
        #     for list in nums:
        #         if n not in list:
        #             present = False
        #             break
            
        #     if present:
        #         res.append(n)
        
        # return sorted(res)
        
        count_map = {}
        
        for i, list in enumerate(nums):
            for j, num in enumerate(list):
                count_map[num] = 1 + count_map.get(num, 0)
                    
        res = []
        for num, count in count_map.items():
            if count == len(nums):
                res.append(num)
                
        return sorted(res)