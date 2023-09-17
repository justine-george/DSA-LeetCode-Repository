class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
#         1 2 2 4
#         seriesSum = 10
#         duplicateSum = 9
#         uniqueSum = 7
        
        n, duplicateSum, uniqueSum = len(nums), sum(nums), sum(set(nums))
        seriesSum = (n * (n + 1)) // 2
        
        return [duplicateSum - uniqueSum, seriesSum - uniqueSum]