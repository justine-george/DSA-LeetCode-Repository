class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first_occur_map = {}

        min_len = float('inf')
        max_freq = 0
        for i, num in enumerate(nums):
            if num not in first_occur_map:
                first_occur_map[num] = i
            count[num] += 1

            if count[num] > max_freq:
                max_freq = count[num]
                min_len = i - first_occur_map[num] + 1
            elif count[num] == max_freq:
                min_len = min(min_len, i - first_occur_map[num] + 1)
        
        return min_len
        
        '''
        # naive solution
        freq_map = Counter(nums)
        
        max_nums, max_count = [], max(freq_map.values())
        for num in freq_map:
            if freq_map[num] == max_count:
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
        '''