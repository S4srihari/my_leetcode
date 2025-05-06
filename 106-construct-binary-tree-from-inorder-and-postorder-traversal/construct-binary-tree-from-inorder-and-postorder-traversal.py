# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def tree(ino,pos):
            if not ino:
                return None
            val = pos.pop()
            root = TreeNode(val)
            idx = ino.index(val)
            root.right = tree(ino[idx+1:],pos)
            root.left = tree(ino[:idx],pos)
            return root
        
        return tree(inorder,postorder)