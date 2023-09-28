class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # iterating backwards using 3 pointers
        # T: O(n + m), Space efficient - O(1)
        i, l, r = len(nums1) - 1, m - 1, n - 1

        while l >= 0 and r >= 0:
            if nums1[l] > nums2[r]:
                nums1[i] = nums1[l]
                l -= 1
            else:
                nums1[i] = nums2[r]
                r -= 1
            i -= 1
        
        while l >= 0:
            nums1[i] = nums1[l]
            l -= 1
            i -= 1
        while r >= 0:
            nums1[i] = nums2[r]
            r -= 1
            i -= 1
        
        # # iterating forward using 3 pointers
        # # T: O(n + m), S: O(m)
        # i, l, r = 0, 0, 0
        # nums1copy = nums1[:m]
        # while l < m and r < n:
        #     if nums1copy[l] <= nums2[r]:
        #         nums1[i] = nums1copy[l]
        #         l += 1
        #     else:
        #         nums1[i] = nums2[r]
        #         r += 1
        #     i += 1
        
        # while l < m:
        #     nums1[i] = nums1copy[l]
        #     i += 1
        #     l += 1
        
        # while r < n:
        #     nums1[i] = nums2[r]
        #     i += 1
        #     r += 1