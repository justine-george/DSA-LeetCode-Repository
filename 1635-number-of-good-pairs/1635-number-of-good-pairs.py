class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # map = {}
        # res = 0
        # for i in range(len(nums)):
        #     if nums[i] in map:
        #         res += len(map[nums[i]])
        #         map[nums[i]].append(i)
        #     else:
        #         map[nums[i]] = [i]
        
        # return res

        # If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.

        count_map = {}
        for i, n in enumerate(nums):
            count_map[n] = count_map.get(n, 0) + 1

        res = 0
        for n, count in count_map.items():
            res += (count * (count - 1) // 2)

        return res