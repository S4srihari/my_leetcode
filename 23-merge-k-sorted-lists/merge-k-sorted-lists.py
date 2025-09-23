# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists : return 
        l = []
        for head in lists:
            node = head
            while node is not None:
                l.append(node)
                node = node.next
        l.sort(key = lambda x : x.val)
        res = None
        for i in range(len(l)):
            if res == None:
                res = l[i]
            else:
                l[i-1].next = l[i]
        return res