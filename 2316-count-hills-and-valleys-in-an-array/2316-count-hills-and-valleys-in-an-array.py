class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hill = []
        valley = []

        for i in range(1, len(nums) - 1):
            if i != 1 and nums[i] == nums[i - 1]:
                continue

            # identify hill
            l, r = i - 1, i + 1
            while l >= 0 and r <= len(nums) - 1:
                if nums[i] > nums[l] and nums[i] > nums[r]:
                    hill.append(nums[i])
                    break
                if nums[i] < nums[l] or nums[i] < nums[r]:
                    break
                
                if nums[i] == nums[l]:
                    l -= 1
                if nums[i] == nums[r]:
                    r += 1

            # identify valley
            l, r = i - 1, i + 1
            while l >= 0 and r <= len(nums) - 1:
                if nums[i] < nums[l] and nums[i] < nums[r]:
                    valley.append(nums[i])
                    break
                if nums[i] > nums[l] or nums[i] > nums[r]:
                    break
                
                if nums[i] == nums[l]:
                    l -= 1
                if nums[i] == nums[r]:
                    r += 1
        
        return len(hill) + len(valley)