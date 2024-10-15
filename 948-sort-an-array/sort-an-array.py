class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, l2):
            m, n = len(l1), len(l2)
            i, j = 0, 0
            res = []
            while i < m and j < n:
                if l1[i] <= l2[j]:
                    res.append(l1[i])
                    i += 1
                else:
                    res.append(l2[j])
                    j += 1
            
            while i < m:
                res.append(l1[i])
                i += 1
            
            while j < n:
                res.append(l2[j])
                j += 1

            return res

        def mergeSort(arr, l, r):
            if l == r:
                return [arr[l]]
            if l < r:
                mid = l + (r - l) // 2
                left = mergeSort(arr, l, mid)
                right = mergeSort(arr, mid + 1, r)
                return merge(left, right)
        
        return mergeSort(nums, 0, len(nums) - 1)