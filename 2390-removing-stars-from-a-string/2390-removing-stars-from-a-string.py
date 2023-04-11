class Solution:
    def removeStars(self, s: str) -> str:
        
        st = collections.deque(s[0])
        i = 1
        # while st and i < len(s):
        #     if s[i] == '*':
        #         st.pop()
        #     else:
        #         st.append(s[i])
        #     i += 1
        # return "".join(st)
    
        for i in range(1, len(s)):
            if s[i] == '*':
                st.pop()
            else:
                st.append(s[i])
            i += 1
        return "".join(st)