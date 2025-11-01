# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        store = set(nums)
        tmp = ListNode(0)
        while head.val in store:
            head = head.next
        res = tmp
        while head:
            if head.val not in store:
                tmp.next = ListNode(head.val)
                tmp = tmp.next
            head = head.next
        return res.next