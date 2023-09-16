class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        map = {}
        
        def getSumDigits(n):
            sum = 0
            while n:
                sum += n % 10
                n = n // 10
            return sum
            # return sum(int(digit) for digit in str(n))
        
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
        for n in nums:
            insertNumIntoDict(getSumDigits(n), n)
        
        res = -1
        for key in map:
            if len(map[key]) == 2:
                res = max(res, map[key][0] + map[key][1])
        
        return res