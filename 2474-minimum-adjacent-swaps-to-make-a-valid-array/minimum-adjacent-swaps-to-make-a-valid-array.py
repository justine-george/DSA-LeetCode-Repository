class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        largest_elem_index, smallest_elem_index = 0, 0
        for i in range(1, n):
            if nums[i] >= nums[largest_elem_index]:
                largest_elem_index = i
            if nums[i] < nums[smallest_elem_index]:
                smallest_elem_index = i

        # largest move 3 -> 5 = 2
        # smallest move 5 -> 0 = 5
        # if crosses, then subtract 1 since 1 swap contributes for both

        res = (n - 1 - largest_elem_index) + (smallest_elem_index)
        if smallest_elem_index > largest_elem_index:
            res -= 1
        
        return res