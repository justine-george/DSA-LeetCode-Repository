class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first_occur_map = {}

        min_len = float('inf')
        max_freq = 0
        for i in range(len(nums)):
            # first_occur_map.setdefault(nums[i], i)
            if nums[i] not in first_occur_map:
                first_occur_map[nums[i]] = i
            count[nums[i]] += 1

            if count[nums[i]] > max_freq:
                max_freq = count[nums[i]]
                min_len = i - first_occur_map[nums[i]] + 1
            elif count[nums[i]] == max_freq:
                min_len = min(min_len, i - first_occur_map[nums[i]] + 1)
        
        return min_len
        
        '''
        # naive solution
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
        '''