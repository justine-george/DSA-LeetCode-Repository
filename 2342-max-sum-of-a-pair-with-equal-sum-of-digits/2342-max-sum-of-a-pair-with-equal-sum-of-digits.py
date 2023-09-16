class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        map = {}
        
        def getSumDigits(n):
            return sum(int(digit) for digit in str(n))
        
        sumArray = [(getSumDigits(n), n) for n in nums]
        
        # dict type: {sumVal: [list with top 2 numbers]}
        def insertNumIntoDict(sumVal, n):
            if sumVal in map:
                map[sumVal].append(n)
                if len(map[sumVal]) > 2:
                    # remove min
                    map[sumVal].remove(min(map[sumVal]))
            else:
                map[sumVal] = [n]

        # fill the map
        for sumVal, n in sumArray:
            insertNumIntoDict(sumVal, n)

            
        def getSumArray(arr):
            sum = 0
            for n in arr:
                sum += n
            return sum
        
        res = -1
        for key in map:
            if len(map[key]) == 2:
                res = max(res, getSumArray(map[key]))
        
        return res