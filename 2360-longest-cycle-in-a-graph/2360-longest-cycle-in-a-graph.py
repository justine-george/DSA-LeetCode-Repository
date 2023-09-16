class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        used = set()
        res = -1
        for i in range(len(edges)):
            slow = i
            fast = edges[i]
            
            while slow not in used and fast >= 0 and edges[fast] >= 0:
                used.add(slow)
                slow = edges[slow]
                fast = edges[edges[fast]]
                if slow != fast:
                    continue
                
                # found the cycle, find length
                length = 1
                pos = edges[slow]
                while pos != slow:
                    length += 1
                    pos = edges[pos]
                res = max(res, length)
                break
                
        return res if res > 0 else -1 