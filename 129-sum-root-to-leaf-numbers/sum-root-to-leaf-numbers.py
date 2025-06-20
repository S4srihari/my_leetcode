# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def tree(node,s):
            nonlocal ans
            s *= 10
            s += node.val
            if not node.left and not node.right:
                ans += s
                return
            if node.left: tree(node.left,s)
            if node.right: tree(node.right,s)
            return
        tree(root,0)
        return ans