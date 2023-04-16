class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # T: O(n), S: O(n)
        res = [0] * len(temperatures)
        st = [] # keep stack monotonic non-increasing, save indexes only
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                index = st.pop()
                res[index] = i - index
            st.append(i)
        return res
    
        
        # T: O(n), S: O(1) - reverse iterate, only constant space
        n = len(temperatures)
        res = [0] * n
        
        for i in range(n - 2, -1, -1):
            curTemp = temperatures[i]
            
            it = i + 1
            while it < n and curTemp > temperatures[it]:
                if res[it] != 0:
                    it += res[it]
                else:
                    break
            res[i] = it - i
            
        return res
#             i = 5
            
#             it = 6
            
#             n = 8
        
        