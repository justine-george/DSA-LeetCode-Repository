class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n <= 1:
            return n

        i, j = 0, 0
        while i < n:
            count = 1
            while i < n - 1 and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            
            chars[j] = chars[i]
            j += 1
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
            
            i += 1

        return j

        # count = 1
        # res = []
        # i = 0
        # while i < n:
        #     prev = chars[i]
        #     res.append(chars[i])
        #     i += 1
        #     while i < n and chars[i] == prev:
        #         count += 1
        #         i += 1
        #     if count > 1:
        #         for digit in str(count):
        #             res.append(digit)
        #         count = 1
            
        # print(res)
        
        # for i in range(len(res)):
        #     chars[i] = res[i]
        
        # chars = chars[:len(res)]
        # return len(chars)
