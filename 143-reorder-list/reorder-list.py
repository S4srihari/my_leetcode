# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head : return None
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        rev = None
        while temp:
            cur = temp.next
            temp.next = rev
            rev = temp
            temp = cur
        
        front = head
        while rev:
            tmp1,tmp2 = front.next,rev.next
            front.next = rev
            rev.next = tmp1
            front, rev = tmp1, tmp2