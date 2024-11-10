class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        # binary search solution to find length of LIS, T: O(nlogn), S: O(n)

        # returns index where num is or the very next index where its supposed to be.
        def get_insert_index(list, num):
            l, r = 0, len(list) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if list[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        N = len(nums)
        pile = [nums[0]]

        for i in range(1, N):
            if nums[i] > pile[-1]:
                pile.append(nums[i])
            else:
                pile[get_insert_index(pile, nums[i])] = nums[i]

        return len(pile)
        '''

        # dp solution: T: O(n^2), S: O(n)
        N = len(nums)
        LIS = [1] * N
        max_lis = 1
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
            max_lis = max(max_lis, LIS[i])
        
        return max_lis