class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # T: O(n), S: O(1)
        n = len(temperatures)
        res = [0] * n
        hottest = 0

        for i in range(n - 1, -1, -1):
            cur_temp = temperatures[i]
            # if cur_temp is hottest, skip, since there is no hotter day in the future
            if cur_temp >= hottest:
                hottest = cur_temp
                continue

            # use the calculated values to find the next hottest
            days = 1
            while temperatures[i + days] <= cur_temp:
                days += res[i + days]
            res[i] = days
        
        return res
        
        
        # # T: O(n), S: O(n)
        # n = len(temperatures)
        # res = [0] * n

        # stack = [] # maintain monotonic decreasing stack
        # for i in range(n):
        #     # current temp is greater than top of the stack
        #     while stack and temperatures[stack[-1]] < temperatures[i]:
        #         index = stack.pop()
        #         res[index] = i - index
        #     stack.append(i)
        
        # return res