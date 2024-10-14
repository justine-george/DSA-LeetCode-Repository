class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        
        max_nums, max_count = [], max(freq_map.values())
        for num in freq_map:
            if freq_map[num] >= max_count:
                max_count = freq_map[num]
                max_nums.append(num)

        first_index, last_index = 0, len(nums) - 1
        min_size = float('inf')
        print(max_nums)
        for candidate in max_nums:
            for i in range(len(nums)):
                if nums[i] == candidate:
                    first_index = i
                    break
            
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == candidate:
                    last_index = i
                    break
            
            min_size = min(min_size, last_index - first_index + 1)
        
        return min_size