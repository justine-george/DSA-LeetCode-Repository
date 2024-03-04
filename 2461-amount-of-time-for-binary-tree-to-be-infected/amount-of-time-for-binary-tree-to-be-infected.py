# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def create_graph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                create_graph(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                create_graph(node.right)

        graph = collections.defaultdict(list)
        create_graph(root)

        q = collections.deque([(start, 0)]) # (node, no of minutes)
        time_taken = 0
        visited = set()
        while q:
            cur_val, time_elapsed = q.popleft()
            visited.add(cur_val)
            time_taken = max(time_taken, time_elapsed)
            for neighbor in graph[cur_val]:
                if neighbor not in visited:
                    q.append((neighbor, time_elapsed + 1))

        return time_taken