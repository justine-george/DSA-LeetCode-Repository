class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
        # calculate prefixSum
        self.preSum = [0] * self.size
        self.preSum[0] = self.nums[0]
        for i in range(1, self.size):
            self.preSum[i] = self.preSum[i - 1] + self.nums[i]
        print(self.preSum)

    def sumRange(self, left: int, right: int) -> int:
        return (self.preSum[right] if right in range(self.size) else 0) - (self.preSum[left - 1] if left - 1 in range(self.size) else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)