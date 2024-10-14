class Solution:
    def longestMountain(self, arr: List[int]) -> int:
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