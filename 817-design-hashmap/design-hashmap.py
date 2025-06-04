class ListNode:
    def __init__(self, key, val, nxt):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap:
    def __init__(self):
        self.size = 10007
        self.mult = 12582917
        self.map = [None for _ in range(self.size)]
    
    def hash(self,key):
        return (key*self.mult)%self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        h = self.hash(key)
        Node = ListNode(key, value, self.map[h])
        self.map[h] = Node

    def get(self, key: int) -> int:
        h = self.hash(key)
        Node = self.map[h]
        while Node:
            if Node.key == key:
                return Node.val
            Node = Node.next
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        Node = self.map[h]
        if not Node :
            return
        if Node.key == key:
            self.map[h] = Node.next
            return
        while Node.next:
            if Node.next.key == key:
                Node.next = Node.next.next
                return
            Node = Node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)