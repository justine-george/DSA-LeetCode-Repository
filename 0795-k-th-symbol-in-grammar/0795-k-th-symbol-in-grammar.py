class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 01
        # 0110
        # 01101001
        # 0110100110010110

        # 1,2 -> 1
        # 3,4 -> 2
        # 5,6 -> 3
        # 7,8 -> 4

        # if k == 1:
        #     return 0
        # elif k % 2:
        #     return self.kthGrammar(n - 1, (k + 1) / 2)
        # else:
        #     val = self.kthGrammar(n - 1, k / 2)
        #     return 0 if val else 1

        # binary search tree solution
        # T: O(n), S: O(1)

        def dfs(n, k, root):
            if n == 1:
                return root
            
            total_nodes = 2 ** (n - 1)

            # right half
            if k > (total_nodes / 2):
                next_root_val = 1 if root == 0 else 0
                return dfs(n - 1, k - (total_nodes / 2), next_root_val)
            else:
                next_root_val = 0 if root == 0 else 1
                return dfs(n - 1, k, next_root_val)
        
        return dfs(n, k, 0)