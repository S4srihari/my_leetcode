# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        
        def tree(l):
            if not l:
                return None
            n = len(l)
            mid = n//2
            root = TreeNode(l[mid])
            root.left = tree(l[:mid])
            root.right = tree(l[mid+1:])
            return root

        return tree(lis)