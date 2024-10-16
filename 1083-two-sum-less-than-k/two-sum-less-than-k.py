class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        def binary_search(arr, i, l, r):
            while l < r:
                mid = l + (r - l + 1) // 2
                if arr[mid] < k - arr[i]:
                    l = mid
                else:
                    r = mid - 1
            return l if arr[l] < k - arr[i] else l - 1

        nums.sort()
        max_so_far = -1
        for i in range(len(nums) - 1):
            idx = binary_search(nums, i, i + 1, len(nums) - 1)

            if idx > i:
                max_so_far = max(max_so_far, nums[i] + nums[idx])

        return max_so_far