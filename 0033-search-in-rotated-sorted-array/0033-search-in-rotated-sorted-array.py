class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # break down into cases (have the image in mind)
              # <l srt portion><r srt portion>
              #               /              
              #              / 
              #             /-----/
              #                  /
              #                 /                      
            # if mid value belongs to left sorted portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                # if target > nums[mid]:
                #     l = mid + 1
                # else: # two options now
                #     if target < nums[l]:
                #         l = mid + 1
                #     else:
                #         r = mid - 1
            else: # means mid value belongs to right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                # if target < nums[mid]:
                #     r = mid - 1
                # else: # two options now
                #     if target > nums[r]:
                #         r = mid - 1
                #     else:
                #         l = mid + 1
        
        return -1