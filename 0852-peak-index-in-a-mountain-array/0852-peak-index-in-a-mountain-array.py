class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # to avoid boundary check for m-1 and m + 1
        l = 1
        r = len(arr) - 2
        
        while l <= r:
            m = (l + r) // 2
            num = arr[m]
            
            lNum = arr[m - 1]
            rNum = arr[m + 1]
            
            # if peak is found
            if num > lNum and num > rNum:
                return m
            
            # ascending part
            if num <= rNum:
                l = m + 1
            else:
                r = m - 1
        
        return -1