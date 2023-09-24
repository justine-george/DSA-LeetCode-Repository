class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
#         [5,3,3,3,5,6,2]
#         # number of non increasing days to the left:
#         left:
#             [0,1,2,3,0,0,1]
            
#         # number of non decreasing days to the right:
#         right:
#             [0,4,3,2,1,0,0]
        
        n = len(security)
        res = []
        left = [0] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                left[i] = left[i - 1] + 1
                
        right = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        
        # there should be atleast time days before and after i
        for i in range(time, n - time):
            if left[i] >= time and right[i] >= time:
                res.append(i)
                
        return res