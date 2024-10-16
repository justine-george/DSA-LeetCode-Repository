class NumArray:

    def __init__(self, nums: List[int]):
        # calculate prefixSum
        self.preSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.preSum[i + 1] = self.preSum[i] + nums[i]
        print(self.preSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)