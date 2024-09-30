class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            # A smaller, B bigger
            A, B = B, A
        
        # binary search to find proper partition boundary
        l, r = 0, len(A) - 1
        total_size = len(A) + len(B)
        half_size = total_size // 2
        while True:
            A_mid = (l + r) // 2
            B_mid = half_size - (A_mid + 1) - 1

            # 4 partition boundary variables
            A_left = A[A_mid] if A_mid >= 0 else float('-inf')
            A_right = A[A_mid + 1] if A_mid + 1 < len(A) else float('inf')
            B_left = B[B_mid] if B_mid >= 0 else float('-inf')
            B_right = B[B_mid + 1] if B_mid + 1 < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                # successful partition
                if total_size % 2:
                    # odd total
                    return min(A_right, B_right)
                else:
                    # even total
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = A_mid - 1
            else:
                l = A_mid + 1

