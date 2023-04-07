class Solution:
    def isValid(self, s: str) -> bool:
        st = collections.deque()
        
        map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for el in s:
            if len(st) == 0:
                st.append(el)
            else:
                curr = st.pop()
                
                if curr in map:
                    if map[curr] != el:
                        st.append(curr)
                        st.append(el)
                else:
                    st.append(curr)
                    st.append(el)
                        
        return True if len(st) == 0 else False