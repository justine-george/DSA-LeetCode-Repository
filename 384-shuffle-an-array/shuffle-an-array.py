class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums


    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        shuffle = self.original[:]
        for i in range(len(shuffle) - 1, -1, -1):
            idx = random.randint(0, i)
            shuffle[i], shuffle[idx] = shuffle[idx], shuffle[i]
        return shuffle
        # shuffled = self.original[:]
        # random.shuffle(shuffled)
        # return shuffled



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()