# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = []
        depths = []
        q.append(root)
        if root.val == x or root.val == y:
            depths.append([-1,0])
        cur_depth = 1
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if node.left:
                    if node.left.val == x or node.left.val == y:
                        depths.append([node.val,cur_depth])
                    q.append(node.left)
                if node.right: 
                    if node.right.val == x or node.right.val == y:
                        depths.append([node.val,cur_depth])
                    q.append(node.right)
            cur_depth += 1
            
        return True if depths[0][1] == depths[1][1] and depths[0][0] != depths[1][0] else False
        