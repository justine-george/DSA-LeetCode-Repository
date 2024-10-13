class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # binary search solution to find length of LIS, T: O(nlogn), S: O(n)

        # returns index where num is or the very next index where its supposed to be.
        def get_index(list, num):
            l, r = 0, len(list) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if num == list[mid]:
                    return mid
                elif num < list[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        N = len(nums)
        arr = []
        for i in range(N):
            idx = get_index(arr, nums[i])
            if idx == len(arr):
                arr.append(nums[i])
            else:
                arr[idx] = nums[i]

        return len(arr)

        '''
        # dp solution: T: O(n^2), S: O(n)
        N = len(nums)
        LIS = [1] * N

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)
        '''