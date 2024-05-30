class Comparator(str):
    def __lt__(x, y):
        return x + y < y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = "".join(sorted(map(str, nums), key=Comparator, reverse=True))
        return "0" if largest_num[0] == "0" else largest_num