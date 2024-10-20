class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        num = nums[-1]
        cnt = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > num:
                for j in range(2, int(nums[i] / 2) + 1):
                    if nums[i] % j == 0:
                        nums[i] = j
                        cnt += 1
                        break

            if nums[i] > num:
                return -1

            num = nums[i]

        return cnt