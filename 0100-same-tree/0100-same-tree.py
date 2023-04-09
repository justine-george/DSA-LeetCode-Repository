# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:   
#         # use recursion
#         if not p and not q:
#             return True
#         if not p or not q or p.val != q.val:
#             return False
        
#         # we need both to be true
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        # iterative solution
        st = [(p, q)]
        while st:
            node1, node2 = st.pop()
            
            if not node1 and not node2:
                continue
            
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            st.append((node1.left, node2.left))
            st.append((node1.right, node2.right))
        return True
    
    
    
    
    
    
    
    
    
    