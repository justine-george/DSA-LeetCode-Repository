class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        used = set()
        res = -1
        for i in range(len(edges)):
            # Use Floyd's algorithm to detect if a loop has been found, marking nodes as we go
            slow = i
            fast = edges[i]
            while slow not in used and 0 <= fast and 0 <= edges[fast]:
                used.add(slow)
                slow = edges[slow]
                fast = edges[edges[fast]]
                if slow != fast:
                    continue

                # Found a loop, now count the length
                size = 1
                pos = edges[fast]
                while pos != fast:
                    size += 1
                    pos = edges[pos]
                res = max(res, size)
                break
        return res