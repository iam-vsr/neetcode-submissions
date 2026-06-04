# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxi=-1001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            ls = max(0,dfs(node.left))
            rs = max(0,dfs(node.right))
            self.maxi=max(self.maxi, ls+rs+node.val)

            return node.val+max(ls,rs)
        
        dfs(root)
        return self.maxi