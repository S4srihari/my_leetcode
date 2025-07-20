# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, a,b):
        res = temp = ListNode(0)
        while a and b:
            if a.val <= b.val:
                temp.next = a
                a = a.next
                temp = temp.next
            else :
                temp.next = b
                b = b.next
                temp = temp.next
        if a: temp.next = a
        if b: temp.next = b
        return res.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists :
            return None
        for idx in range(1,len(lists)):
            lists[idx] = self.merge2Lists(lists[idx-1],lists[idx])
        return lists[-1]