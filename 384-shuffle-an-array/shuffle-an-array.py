class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.shuffled_nums = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        for i in range(len(self.shuffled_nums) - 1, -1, -1):
            idx = random.randint(0, i)
            self.swap(self.shuffled_nums, i, idx)
        return self.shuffled_nums
    
    def swap(self, list, idx1, idx2):
        list[idx1], list[idx2] = list[idx2], list[idx1]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()