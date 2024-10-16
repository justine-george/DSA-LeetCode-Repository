class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        def binary_search_highest(arr, l, r, i, k):
            while l < r:
                mid = l + (r - l + 1) // 2
                if arr[mid] + arr[i] < k:
                    l = mid
                else:
                    r = mid - 1
            return l if arr[l] + arr[i] < k else l - 1

        nums.sort()
        max_so_far = -1
        for i in range(len(nums) - 1):
            if nums[i] >= k:
                break

            j = binary_search_highest(nums, i + 1, len(nums) - 1, i, k)
            if j > i:
                max_so_far = max(max_so_far, nums[i] + nums[j])

        return max_so_far