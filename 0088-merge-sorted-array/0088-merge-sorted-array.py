class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, l, r = 0, 0, 0
        nums1copy = nums1[:m]
        while l < len(nums1copy) and r < len(nums2):
            if nums1copy[l] <= nums2[r]:
                nums1[i] = nums1copy[l]
                l += 1
            else:
                nums1[i] = nums2[r]
                r += 1
            i += 1
        
        while l < len(nums1copy):
            nums1[i] = nums1copy[l]
            i += 1
            l += 1
        
        while r < len(nums2):
            nums1[i] = nums2[r]
            i += 1
            r += 1