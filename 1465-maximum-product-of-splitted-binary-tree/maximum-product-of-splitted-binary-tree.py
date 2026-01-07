# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        res = 0
        tot = 0
        mod = 10**9 + 7
        if not root:
            return None
        def dfs(root):
            nonlocal tot
            if not root:
                return 0
            root.val += dfs(root.left)
            root.val += dfs(root.right)
            tot = root.val
            return root.val
        dfs(root)

        def dfs2(root):
            nonlocal res
            nonlocal tot
            if root.left:
                prod = (tot-root.left.val) * root.left.val
                res = max(res, prod)
                dfs2(root.left)
            if root.right:
                prod2 = (tot-root.right.val) * root.right.val
                res = max(res, prod2)
                dfs2(root.right)
            return 

        dfs2(root)

        return res%mod