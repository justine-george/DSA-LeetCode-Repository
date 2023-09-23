# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # initially, we find the peak using binary search
        peakIndex = self.getPeakIndex(mountain_arr)
        
        # now search for the target from start to peakIndex
        targetIndex = self.getTarget(mountain_arr, 0, peakIndex, target)
        if targetIndex != -1:
            return targetIndex
        
        # finally search for the target from peakIndex + 1 to end
        return self.getTarget(
            mountain_arr, peakIndex + 1, mountain_arr.length() - 1, target, True)
    
    # return index of the target
    def getTarget(self, mountain_arr, start, end, target, isDescending = False):
        l = start
        r = end
        
        while l <= r:
            m = (l + r) // 2
            num = mountain_arr.get(m)
            
            # if target is found:
            if num == target:
                return m
            elif num < target:
                if not isDescending:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if not isDescending:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
    
    # return index of the peak of the mountain
    def getPeakIndex(self, mountain_arr):
        arrLength = mountain_arr.length()
        l = 1
        r = arrLength - 2
        
        
        while l <= r :
            m = (l + r) // 2
            
            num = mountain_arr.get(m)
            
            lNum = mountain_arr.get(m - 1)
            rNum = mountain_arr.get(m + 1)

            # if peak is found:
            if num > lNum and num > rNum:
                return m

            # if in the left half
            if lNum <= num <= rNum:
                l = m + 1

            # if in the right half
            if lNum >= num >= rNum:
                r = m - 1
            
        return -1