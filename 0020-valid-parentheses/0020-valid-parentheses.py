class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for el in s:
            if st and map.get(st[-1]) == el:
                st.pop()
            else:
                st.append(el)
                        
        return not st