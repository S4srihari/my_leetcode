# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def solve(root):
            if not root:
                return (True, 0)
            left = solve(root.left)
            right = solve(root.right)
            if not left[0] or not right[0]:
                return (False, 0)
            elif abs(left[1] - right[1]) > 1:
                return (False, 0)
            else:
                return (True, max(left[1],right[1])+1)
        
        ans = solve(root)
        return ans[0]
