class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # T: O(n), S: O(1) - reverse iterate, only constant space
        n = len(temperatures)
        res = [0] * n
        
        for i in range(n - 1, -1, -1):
            it = i + 1
            while it < n:
                if temperatures[it] > temperatures[i]:
                    res[i] = it - i
                    break
                elif res[it] == 0:
                    break
                else:
                    it += res[it]

        return res
    
        # # T: O(n), S: O(n)
        # res = [0] * len(temperatures)
        # st = [] # keep stack monotonic non-increasing, save indexes only
        # for i in range(len(temperatures)):
        #     while st and temperatures[st[-1]] < temperatures[i]:
        #         index = st.pop()
        #         res[index] = i - index
        #     st.append(i)
        # return res