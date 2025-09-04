# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head : return None
        fast,slow,temp = head,head,head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        k = k%size
        if k == 0: return head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        if slow.next: 
            ans = slow.next
        else:
            ans = head
        fast.next = head
        slow.next = None
        return ans