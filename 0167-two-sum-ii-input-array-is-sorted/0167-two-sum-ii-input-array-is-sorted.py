class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l <= r:
            sum = numbers[l] + numbers[r]
            
            if target == sum:
                return [l + 1, r + 1]
            elif target < sum:
                r -= 1
            else:
                l += 1
        
        return [-1, - 1] 