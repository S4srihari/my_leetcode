# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        def traversal(node,cursum,lis):
            nonlocal targetSum
            if not node.left and not node.right:
                if cursum + node.val == targetSum : 
                    lis.append(node.val)
                    ans.append(lis)
                    return
                else :
                    return
            cursum += node.val
            lis.append(node.val)
            if node.left: traversal(node.left,cursum,lis[:])
            if node.right: traversal(node.right,cursum,lis[:])
            return
        traversal(root,0,[])
        return ans
            