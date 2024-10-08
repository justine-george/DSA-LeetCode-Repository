class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()

            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, N - 1)

            for j in range(start, end + 1):
                if s[j] == "0":
                    if j == N - 1:
                        return True
                    q.append(j)
            
            farthest = end
        
        return False