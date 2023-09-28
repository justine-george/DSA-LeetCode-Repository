class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        res = []
        while l < m and r < len(nums2):
            if nums1[l] <= nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        
        while l < m:
            res.append(nums1[l])
            l += 1
        
        while r < len(nums2):
            res.append(nums2[r])
            r += 1
        
        for i in range(len(nums1)):
            nums1[i] = res[i]