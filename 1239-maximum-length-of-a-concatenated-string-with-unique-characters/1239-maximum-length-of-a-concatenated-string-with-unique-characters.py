class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charset = set()
        
        def overlap(s):
            prev = set()
            for c in s:
                if c in charset or c in prev:
                    return True
                prev.add(c)
            return False
        
        def backtrack(i):
            if i == len(arr):
                return len(charset)
            
            res=0
            if not overlap(arr[i]):
                # add arr[i] to charset
                for c in arr[i]:
                    charset.add(c)
                res = backtrack(i + 1)
                # remove arr[i] from charset
                for c in arr[i]:
                    charset.remove(c)
            return max(res, backtrack(i + 1))
        
        return backtrack(0)