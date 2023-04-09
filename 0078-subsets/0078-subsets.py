class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # backtracking solution
        # i - index
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
    
#     [1, 2, 3]
# recursion stack shown below:
# dfs(0):
#     s = [1]
#     dfs(1):
#         s = [1, 2]
#         dfs(2):
#             s = [1, 2, 3]
#             dfs(3):
#                 res = [[1, 2, 3]]
#             s = [1, 2]
#             dfs(3):
#                 res = [..., [1, 2]]
#         s = [1]
#         dfs(2):
#             s = [1, 3]
#             dfs(3):
#                 res = [..., [1, 3]]
#             s = [1]
#             dfs(3):
#                 res = [..., [1]]
#     s = []
#     dfs(1):
#         s = [2]
#         dfs(2):
#             s = [2, 3]
#             dfs(3):
#                 res = [..., [2, 3]]
#             s = [2]
#             dfs(3):
#                 res = [..., [2]]
#         s = []
#         dfs(2):
#             s = [3]
#             dfs(3):
#                 res = [..., [3]]
#             s = []
#             dfs(3):
#                 res = [..., []]
# finally, res =        