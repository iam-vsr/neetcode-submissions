# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val=-1001
        def dfs(node):
            nonlocal max_val

            if not node:
                return 0
            ls=max(0,dfs(node.left))
            rs=max(0,dfs(node.right))
            max_val=max(max_val,node.val+ls+rs)
            return node.val+max(ls,rs)
        
        dfs(root)
        return max_val