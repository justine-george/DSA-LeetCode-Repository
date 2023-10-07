class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

            if len(count) <= 2: continue

            new_count = {}
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            
            count = new_count
        
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res