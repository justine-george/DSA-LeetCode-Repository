class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.shuffled_nums = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        for i in range(len(self.shuffled_nums) - 1, -1, -1):
            idx = random.randint(0, i)
            self.shuffled_nums[i], self.shuffled_nums[idx] = self.shuffled_nums[idx], self.shuffled_nums[i]
        return self.shuffled_nums
        # shuffled = self.original[:]
        # random.shuffle(shuffled)
        # return shuffled



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()