# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mini_level = 1
        max_level_sum = root.val
        que = deque([root])
        level =  1
        while que:
            length = len(que)
            cur_level_sum = 0
            for _ in range(length):
                node = que.popleft()
                cur_level_sum += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if cur_level_sum > max_level_sum:
                mini_level = level
                max_level_sum = cur_level_sum
            level += 1
        return mini_level
            