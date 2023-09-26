class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            a_partition = (l + r) // 2
            b_partition = half - a_partition - 2

            a_left = A[a_partition] if a_partition >= 0 else float('-inf')
            a_right = A[a_partition + 1] if (a_partition + 1) < len(A) else float('inf')
            b_left = B[b_partition] if b_partition >= 0 else float('-inf')
            b_right = B[b_partition + 1] if (b_partition + 1) < len(B) else float('inf')

            # correct partition
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)
                # even
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            
            # if a_partition is too far right
            if a_left > b_right:
                r = a_partition - 1
            else:
                l = a_partition + 1