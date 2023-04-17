class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        
        res = [False] * len(candies)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandy:
                res[i] = True
        
        return res