class DetectSquares:

    def __init__(self):
        self.hashSet = defaultdict(int)
        self.nodes = []

    def add(self, point: List[int]) -> None:
        self.hashSet[tuple(point)] += 1
        self.nodes.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        X,Y = point
        for x,y in self.nodes:
            if X == x or Y == y or abs(X-x) != abs(Y-y):
                continue
            res += self.hashSet[(x,Y)] * self.hashSet[(X,y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)