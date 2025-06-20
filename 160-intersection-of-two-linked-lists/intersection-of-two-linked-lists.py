# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_set = set()
        while headA and headB:
            if headA in hash_set:
                return  headA
            hash_set.add(headA)
            headA = headA.next
            if headB in hash_set:
                return headB
            hash_set.add(headB)
            headB = headB.next

        while headA:
            if headA in hash_set:
                return   headA
            hash_set.add(headA)
            headA = headA.next
        
        while headB:
            if headB in hash_set:
                return headB
            hash_set.add(headB)
            headB = headB.next