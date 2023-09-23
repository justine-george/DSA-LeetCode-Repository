class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # to avoid boundary check for m-1 and m + 1
        l = 1
        r = len(arr) - 2
        
        while l <= r:
            m = (l + r) // 2
            
            # if peak is found
            if arr[m] > arr[m - 1] and arr[m] > arr[m + 1]:
                return m
            
            # ascending part
            if arr[m] <= arr[m + 1]:
                l = m + 1
            else:
                r = m - 1
        
        return -1