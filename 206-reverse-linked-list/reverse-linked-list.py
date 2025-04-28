# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """if not head:
            return None
        temp = ListNode(head.val)
        answer = temp
        head = head.next
        while head:
            temp = ListNode(head.val)
            temp.next = answer
            answer = temp
            head = head.next
        return answer"""

        if not head :
            return None 
        prev = None 
        curr = None
        while head:
            curr = ListNode(head.val)
            curr.next = prev
            prev = curr
            head = head.next
        return curr