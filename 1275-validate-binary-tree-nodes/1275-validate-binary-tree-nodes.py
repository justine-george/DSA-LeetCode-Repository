class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)

        # if every element has a parent, not a tree (root node doesn't have a parent)
        if len(hasParent) == n:
            return False

        # find out the root
        root = -1
        for i in range(n):
            if i not in leftChild and i not in rightChild:
                root = i
                break
        
        visited = set()
        stack = [root]
        while stack:
            cur = stack.pop()

            # cycle detected
            if cur in visited:
                return False
            visited.add(cur)

            # go to left child
            if leftChild[cur] != -1:
                stack.append(leftChild[cur])
            # go to right child
            if rightChild[cur] != -1:
                stack.append(rightChild[cur])
        
        # if all elements in visited, then tree is connected
        return len(visited) == n