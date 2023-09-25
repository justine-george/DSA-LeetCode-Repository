class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Time complexity:
            O(log(min(A, B)))
        
        Space complexity:
            O(1)
        """
        
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # for A, the smaller list
            j = half - i - 2 # for B
            
            a_left = A[i] if i >= 0 else float('-inf')
            a_right = A[i + 1] if (i + 1) < len(A) else float('inf')
            b_left = B[j] if j >= 0 else float('-inf')
            b_right = B[j + 1] if (j + 1) < len(B) else float('inf')
            
            # if partition is right
            if a_left <= b_right and b_left <= a_right:
                # odd number of elements in total
                if total % 2:
                    return min(a_right, b_right)
                # even number of elements in total
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            
            # a partition is too big, reduce it by half
            if a_left > b_right:
                r = i - 1
            else:
                l = i + 1