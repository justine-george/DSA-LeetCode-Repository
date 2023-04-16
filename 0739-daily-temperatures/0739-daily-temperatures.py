class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # st = [(temperatures[0], 0)]
        st = []
        for i in range(len(temperatures)):
            while st and st[-1][0] < temperatures[i]:
                val, index = st.pop()
                res[index] = i - index
            st.append((temperatures[i], i))
        
        return res