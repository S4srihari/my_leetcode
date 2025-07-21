# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        if root.left: 
            if self.isSubtree(root.left,subRoot):
                return True
        if root.right: 
            if self.isSubtree(root.right,subRoot):
                return True
        return False