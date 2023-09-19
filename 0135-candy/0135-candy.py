class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
                
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
        
        return sum(res)
    
    
#     1 0 2
    
#     1st pass
#     res
#     [1 1 2]
    
#     2nd pass, from end
#     res
#     [1 1 2]