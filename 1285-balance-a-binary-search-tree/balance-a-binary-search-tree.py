# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def flatten(root):
            if not root:
                return
            if root.left:
                flatten(root.left)
            values.append(root.val)
            if root.right:
                flatten(root.right)
        
        flatten(root)

        def construct(vals):
            n = len(vals)
            if n == 0:
                return None
            elif n == 1:
                return TreeNode(vals[0])
            else:
                root = TreeNode(vals[n//2])
                root.left = construct(vals[:n//2])
                root.right = construct(vals[n//2+1:])
                return root
        
        return construct(values)