# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head:
            temp = head.next
            head.next = rev
            rev = head
            head = temp
        return rev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = dummy = last_div = ListNode(0)
        last_div.next = head 
        cnt = 0
        while head:
            cnt += 1
            if cnt%k == 0:
                temp = head.next
                head.next = None
                last_div.next = self.reverse(last_div.next)
                dummy.next = last_div.next
                while last_div.next:
                    last_div = last_div.next
                    dummy = dummy.next
                last_div.next = temp
                head = temp
            else : head = head.next
        dummy.next = last_div.next
        return res.next