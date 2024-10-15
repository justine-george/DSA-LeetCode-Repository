class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, l2):
            i, j = 0, 0
            res = []
            while i < len(l1) and j < len(l2):
                if l1[i] <= l2[j]:
                    res.append(l1[i])
                    i += 1
                else:
                    res.append(l2[j])
                    j += 1

            if i < len(l1):
                res.extend(l1[i:])
            if j < len(l2):
                res.extend(l2[j:])

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