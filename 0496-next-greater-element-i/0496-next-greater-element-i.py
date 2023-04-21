class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonic stack - keep it non increasing
        st = []
        
        map = {} # stores {el: next greatest to el} mapping
        for num in nums2:
            while st and st[-1] < num:
                top = st.pop()
                map[top] = num
            st.append(num)
            
        return [map.get(num, -1) for num in nums1]