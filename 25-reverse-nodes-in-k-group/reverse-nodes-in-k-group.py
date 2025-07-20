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
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr = head
        count = 0

        while curr:
            count += 1
            if count % k == 0:
                group_start = prev_group_tail.next
                next_group_head = curr.next
                curr.next = None  # Temporarily break the group

                # Reverse the current k-group
                reversed_head = self.reverse(group_start)

                # Reconnect with the previous part
                prev_group_tail.next = reversed_head
                group_start.next = next_group_head  # group_start is new tail

                # Move to the next group
                prev_group_tail = group_start
                curr = next_group_head
            else:
                curr = curr.next

        return dummy.next