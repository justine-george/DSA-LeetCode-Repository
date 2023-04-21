class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonic stack - keep it non increasing
        st = [nums2[0]]
        
        map = {} # stores {el: next greatest to el} mapping
        for i in range(1, len(nums2)):
            while st and st[-1] < nums2[i]:
                top = st.pop()
                map[top] = nums2[i]
            st.append(nums2[i])
            
        return [map[n] if n in map else -1 for n in nums1]