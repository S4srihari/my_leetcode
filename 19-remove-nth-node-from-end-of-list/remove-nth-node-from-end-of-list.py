# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0: return head
        fast = head
        for _ in range(n):
            fast = fast.next
        slow = ListNode(0)
        slow.next = head
        ans = slow
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return ans.next