class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        largest_elem_index = 0
        for i in range(1, n):
            if nums[i] >= nums[largest_elem_index]:
                largest_elem_index = i

        smallest_elem_index = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[smallest_elem_index]:
                smallest_elem_index = i
        
        # print(largest_elem_index)
        # print(smallest_elem_index)
        # return 0

        # 3 -> 5
        # 0 <- 5

        res = (n - 1 - largest_elem_index) + (smallest_elem_index)
        if smallest_elem_index > largest_elem_index:
            res -= 1
        
        return res