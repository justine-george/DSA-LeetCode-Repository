class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 12234567
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            while l > 0 and l < n and numbers[l] == numbers[l - 1]:
                l += 1
            
            while r < n - 1 and r >= 0 and numbers[r] == numbers[r + 1]:
                r -= 1

            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]