# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        s = []
        def dfs(root,v):
            v += root.val
            if not root.left and not root.right:
                s.append(v)
                return
            if root.left:
                dfs(root.left,v)
            if root.right:
                dfs(root.right,v)
            return
        if not root :
            return False
        dfs(root,0)
        
        return targetSum in s
