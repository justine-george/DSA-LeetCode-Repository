class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # dict type: {sumVal: [list with top 2 numbers]}
        map = {}
        
        def getSumDigits(n):
            sum = 0
            while n:
                sum += n % 10
                n = n // 10
            return sum

        # fill the map
        for n in nums:
            sumVal = getSumDigits(n)
            if sumVal in map:
                map[sumVal].append(n)
                if len(map[sumVal]) > 2:
                    # remove min
                    map[sumVal].remove(min(map[sumVal]))
            else:
                map[sumVal] = [n]
        
        return max((map[key][0] + map[key][1] for key in map if len(map[key]) == 2), default = -1)