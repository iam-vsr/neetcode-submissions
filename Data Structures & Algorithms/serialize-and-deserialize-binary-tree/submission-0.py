# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#'
        res=[]
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals=data.split(",")
        if vals[0]=='#':
            return None

        root=TreeNode(int(vals[0]))
        queue=deque([root])
        idx=1

        while queue:
            node=queue.popleft()
            if vals[idx]!='#':
                node.left=TreeNode(int(vals[idx]))
                queue.append(node.left)
            idx+=1
            if vals[idx]!='#':
                node.right=TreeNode(int(vals[idx]))
                queue.append(node.right)
            idx+=1
        return root
