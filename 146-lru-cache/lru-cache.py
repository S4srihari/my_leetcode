class LRUCache:

    def __init__(self, capacity: int):
        self.dic = defaultdict(int)
        self.lis = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        val = -1
        if key in self.lis:
            self.lis.remove(key)
            self.lis.append(key)
            val = self.dic[key]
        return val

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
        if key in self.lis:
            self.lis.remove(key)
        self.lis.append(key)
        if len(self.lis) > self.capacity:
            self.lis.pop(0)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)