class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        seen = set()
        while True:
            if num == 1:
                return True
            sum = 0
            while num != 0:
                r = num % 10
                sum += (r * r)
                num //= 10
            num = sum
            if num in seen:
                return False
            seen.add(num)