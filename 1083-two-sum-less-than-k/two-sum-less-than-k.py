class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        def binary_search(arr, i, l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] < k - arr[i]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        nums.sort()
        max_so_far = -1
        for i in range(len(nums) - 1):
            idx = binary_search(nums, i, i + 1, len(nums) - 1)
            # idx = bisect.bisect_left(nums, k - nums[i]) - 1
            # if idx == i:
            #     idx -= 1

            if idx > i:
                max_so_far = max(max_so_far, nums[i] + nums[idx])

        return max_so_far