# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None
        fast, slow = head, head
        cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle = True
                break
        if not cycle : return None
        else :
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
        return slow
