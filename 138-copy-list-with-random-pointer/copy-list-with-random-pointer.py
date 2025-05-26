"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashing = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            hashing[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = hashing[cur]
            copy.next = hashing[cur.next]
            copy.random = hashing[cur.random]
            cur = cur.next

        return hashing[head] 