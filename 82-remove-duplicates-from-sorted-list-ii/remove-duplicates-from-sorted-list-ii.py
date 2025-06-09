# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        ans = temp
        cur = None
        while head and head.next:
            if head.val != head.next.val and head.val != cur:
                temp.next = ListNode(head.val)
                temp = temp.next
            cur = head.val
            head = head.next
            
        if head and head.val != cur:
            temp.next = ListNode(head.val)
            temp = temp.next
        return ans.next
                