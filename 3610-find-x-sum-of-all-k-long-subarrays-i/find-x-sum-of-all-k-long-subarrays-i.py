class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def do_sum(i):
            ctr = Counter(nums[i:i + k])
            most_freq = heapq.nlargest(x, ctr, key=lambda y: (ctr[y], y))
            return sum(y * ctr[y] for y in most_freq)
            
        return list(map(do_sum, range(len(nums) - k + 1)))