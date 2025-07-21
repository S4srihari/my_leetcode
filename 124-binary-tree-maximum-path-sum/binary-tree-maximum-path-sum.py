# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = -float("inf")
        def maxPath(root):
            if not root: return -float("inf")
            left = maxPath(root.left)
            right = maxPath(root.right)
            self.maxi = max(self.maxi, root.val+left+right, root.val+left, root.val+right, root.val, left, right)
            return max(root.val+left, root.val+right, root.val)
        maxPath(root)
        return self.maxi