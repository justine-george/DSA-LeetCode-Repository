class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        n = len(chars)
        res = []
        i = 0
        while i < n:
            prev = chars[i]
            res.append(chars[i])
            i += 1
            while i < n and chars[i] == prev:
                count += 1
                i += 1
            if count > 1:
                for digit in str(count):
                    res.append(digit)
                count = 1
            
        print(res)
        
        for i in range(len(res)):
            chars[i] = res[i]
        
        chars = chars[:len(res)]
        return len(chars)
