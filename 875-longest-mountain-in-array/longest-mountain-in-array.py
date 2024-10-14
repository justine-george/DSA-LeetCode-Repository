class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # T: O(n), S: O(1)
        N = len(arr)
        if N < 3:
            return 0

        max_length = 0
        i = 1

        while i < N - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                right = i + 1
                while right < N - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                max_length = max(max_length, right - left + 1)
                i = right
            else:
                i += 1
        
        return max_length

        '''
        if len(arr) < 3:
            return 0

        peaks = []
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                peaks.append(i)

        max_length = 0
        for peak_idx in peaks:
            l = peak_idx - 1
            while l >= 0 and arr[l] < arr[l + 1]:
                l -= 1
            l += 1
            
            r = peak_idx + 1
            while r < len(arr) and arr[r] < arr[r - 1]:
                r += 1
            r -= 1

            max_length = max(max_length, r - l + 1)

        return max_length
        '''