# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return 
        ran = 0
        heap = []
        temp = ListNode()
        res = temp
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, ran, lists[i]))
                ran += 1
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap)
            temp.next = node[2]
            temp = temp.next
            if temp.next is not None: 
                heapq.heappush(heap,(temp.next.val, ran, temp.next))
                ran += 1
        return res.next