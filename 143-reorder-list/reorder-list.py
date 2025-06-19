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
        prev = cur = None
        size = 0
        temp = head
        while temp:
            size += 1
            cur = ListNode(temp.val)
            cur.next = prev
            prev = cur
            temp = temp.next
        temp = head.next
        for i in range(1,size):
            if i%2 == 1:
                head.next = prev
                head = head.next
                prev = prev.next
            else :
                head.next = temp
                temp = temp.next
                head = head.next
        head.next = None