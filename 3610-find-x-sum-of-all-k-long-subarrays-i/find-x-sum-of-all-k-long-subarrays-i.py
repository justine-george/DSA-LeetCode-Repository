class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def custom_comparator(x):
            return (-x[0], -x[1])
        
        def compute_next_res(counter_map, res):
            freq_list = [(freq, key) for key, freq in counter_map.items()]
            freq_list.sort(key=custom_comparator)
            x_sum= sum(freq_list[i][0] * freq_list[i][1] for i in range(x) if i < len(freq_list))
            res.append(x_sum)

        counter_map = defaultdict(int)
        for i in range(k):
            counter_map[nums[i]] += 1
        
        res = []
        compute_next_res(counter_map, res)

        l, r = 0, k
        while r < len(nums):
            counter_map[nums[r]] += 1
            counter_map[nums[l]] -= 1
            compute_next_res(counter_map, res)

            l, r = l + 1, r + 1
        
        return res
                