class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [-1] * n
        
        def traverse(start):
            path = []
            curr = start
            seen = {}
            idx = 0
            
            while curr not in seen and ans[curr] == -1:
                seen[curr] = idx
                path.append(curr)
                curr = edges[curr]
                idx += 1

            # If the node was seen before, it's part of a loop
            if curr in seen:
                loop_len = idx - seen[curr]
                for _ in range(loop_len):
                    ans[path.pop()] = loop_len
                
                # For nodes leading up to the loop
                value = loop_len + 1
                while path:
                    ans[path.pop()] = value
                    value += 1
            else:  # If the node's value is already computed
                value = ans[curr] + 1
                while path:
                    ans[path.pop()] = value
                    value += 1

        for i in range(n):
            if ans[i] == -1:
                traverse(i)
        
        return ans