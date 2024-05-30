class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = map(str, nums)

        sorted_nums = "".join(sorted(str_nums, key=LargerNumKey))

        return "0" if sorted_nums[0] == '0' else sorted_nums
