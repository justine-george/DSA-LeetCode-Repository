class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        map = {3: "Fizz", 5: "Buzz"}
        for i in range(1, n + 1):
            temp = ""
            for key in map:
                if i % key == 0:
                    temp += map[key]
            if temp == "":
                temp += str(i)
            res.append(temp)
        
        return res