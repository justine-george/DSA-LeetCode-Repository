class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        max_so_far = -1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum < k:
                max_so_far = max(max_so_far, cur_sum)
                l += 1
            else:
                r -= 1
        
        return max_so_far

        '''
        def binary_search_highest(arr, l, r, target):
            while l < r:
                mid = l + (r - l + 1) // 2
                if arr[mid] < target:
                    l = mid
                else:
                    r = mid - 1
            return l if arr[l] < target else l - 1

        nums.sort()
        max_so_far = -1
        for i in range(len(nums) - 1):
            if nums[i] >= k:
                break

            j = binary_search_highest(nums, i + 1, len(nums) - 1, k - nums[i])
            if j > i:
                max_so_far = max(max_so_far, nums[i] + nums[j])

        return max_so_far
        '''