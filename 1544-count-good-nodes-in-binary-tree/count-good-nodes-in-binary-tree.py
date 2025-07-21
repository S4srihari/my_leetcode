# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        que = deque([(-float("inf"),root)])
        while que:
            prev_max, node = que.popleft()
            if node.val >= prev_max:
                res += 1
                prev_max = node.val
            if node.left: que.append((prev_max, node.left))
            if node.right: que.append((prev_max, node.right))
        return res