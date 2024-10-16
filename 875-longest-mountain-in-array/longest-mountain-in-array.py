class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # T: O(n), S: O(1)
        N = len(arr)
        if N < 3:
            return 0

        max_length = 0

        i = 1
        # iterate from [1 to N - 2]
        while i < N - 1:
            # found peak
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