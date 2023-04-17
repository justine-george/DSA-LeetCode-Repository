class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # mid = (l + r) // 2
            # to prevent overflow, l + half-distance bw l and r
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
    
#         def binSearch(l, r):
#             if l > r:
#                 return -1
            
#             mid = l + (r - l) // 2
            
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 return binSearch(l, mid - 1)
#             else:
#                 return binSearch(mid + 1, r)
        
#         return binSearch(l, r)