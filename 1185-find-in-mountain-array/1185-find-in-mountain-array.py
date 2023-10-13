# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def get_peak():
            # peak can be from 1 to len - 2
            start = 1
            end = mountain_arr.length() - 2
            while start <= end:
                m = (start + end) // 2
                cur = mountain_arr.get(m)
                left = mountain_arr.get(m - 1)
                right = mountain_arr.get(m + 1)
                
                if left < cur < right:
                    start = m + 1
                elif left > cur > right:
                    end = m - 1
                else:
                    return m
            return start
        
        def bin_search(start, end, left):
            while start <= end:
                m = (start + end) // 2
                cur = mountain_arr.get(m)

                if cur == target:
                    return m
                elif cur > target:
                    if left:
                        end = m - 1
                    else:
                        start = m + 1
                else:
                    if left:
                        start = m + 1
                    else:
                        end = m - 1
            return -1

        peak = get_peak()

        leftI = bin_search(0, peak, True)
        if leftI != -1:
            return leftI
        
        if mountain_arr.get(peak) == target:
            return peak
        
        return bin_search(peak + 1, mountain_arr.length() - 1, False)