# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def tree(pre,ino):
            if not pre or not ino:
                return None
            l_size = ino.index(pre[0])
            root = TreeNode(pre.pop(0))
            root.left = tree(pre[:l_size],ino[:l_size])
            root.right = tree(pre[l_size:],ino[l_size+1:])
            return root
        
        return tree(preorder,inorder)