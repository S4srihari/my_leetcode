# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p,q = q,p
        while root:
            if root.val >= p.val and root.val <= q.val:
                return root
            elif root.val < p.val:
                root = root.right
            else:
                root = root.left
        return None
        