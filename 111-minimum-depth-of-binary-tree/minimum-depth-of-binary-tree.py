# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def mdepth(root):
            if not root: return 0
            if not root.left and not root.right: return 1
            rd = mdepth(root.right)
            ld = mdepth(root.left)
            if not root.left: return rd + 1
            if not root.right: return ld + 1
            return min(ld,rd)+ 1

            
        return  mdepth(root) 