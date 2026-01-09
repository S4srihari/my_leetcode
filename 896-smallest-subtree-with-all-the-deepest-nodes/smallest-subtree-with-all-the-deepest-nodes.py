# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def depth(node):
            if not node :
                return 0
            return 1 + max(depth(node.left),depth(node.right))

        node = root
        ans = root
        while True:
            if depth(node.left) == depth(node.right):
                return ans
                break
            elif depth(node.left) > depth(node.right):
                node = node.left
            else :
                node = node.right
            ans = node