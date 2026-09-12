# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map={}
        for i in range(len(inorder)):
            in_map[inorder[i]] = i

        def f(pre_start, pre_end, in_start, in_end):
            if pre_start>pre_end or in_start>in_end:
                return None
            
            root=TreeNode(preorder[pre_start])
            in_root=in_map[root.val]

            left_nums=in_root-in_start

            root.left=f(pre_start+1, pre_start+left_nums, in_start, in_root-1)
            root.right=f(pre_start+left_nums+1, pre_end, in_root+1, in_end)

            return root
        
        return f(0, len(preorder)-1, 0, len(inorder)-1)

