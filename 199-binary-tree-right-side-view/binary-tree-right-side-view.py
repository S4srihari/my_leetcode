# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        q = []
        q.append(root)
        while q:
            ans.append(q[0].val)
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return ans