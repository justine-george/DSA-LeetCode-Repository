# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.graph = collections.defaultdict(list)
        self.create_graph(root)

        q = collections.deque([(start, 0)]) # (node, no of minutes)
        time_taken = 0
        visited = set()
        while q:
            cur_val, time_elapsed = q.popleft()
            visited.add(cur_val)
            time_taken = max(time_taken, time_elapsed)
            for neighbor in self.graph[cur_val]:
                if neighbor not in visited:
                    q.append((neighbor, time_elapsed + 1))

        return time_taken
    
    def create_graph(self, node):
        if not node:
            return

        if node.left:
            self.graph[node.val].append(node.left.val)
            self.graph[node.left.val].append(node.val)
            
        if node.right:
            self.graph[node.val].append(node.right.val)
            self.graph[node.right.val].append(node.val)
        
        self.create_graph(node.left)
        self.create_graph(node.right)