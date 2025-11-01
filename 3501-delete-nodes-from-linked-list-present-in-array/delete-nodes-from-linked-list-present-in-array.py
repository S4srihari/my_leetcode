# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        store = set(nums)
        while head and head.val in store:
            head = head.next
        prev = head
        res = head
        if head.next:
            head = head.next
            while head:
                if head.val not in store:
                    prev.next = head
                    prev = prev.next
                head = head.next
            if prev.next and prev.next.val in store:
                prev.next = None
        return res