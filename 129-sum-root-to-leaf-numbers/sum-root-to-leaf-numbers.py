# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def tree(node,s):
            value = node.val
            s += str(value)
            if not node.left and not node.right:
                ans.append(s)
                return
            if node.left: tree(node.left,s)
            if node.right: tree(node.right,s)
            return
        tree(root,"")
        return sum([int(i) for i in ans])