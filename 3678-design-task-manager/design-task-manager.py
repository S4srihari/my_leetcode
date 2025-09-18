class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskHeap = []
        self.priorityHash = defaultdict(int)
        self.userHash = defaultdict(int)
        for uId, tId, pr in tasks:
            self.taskHeap.append((-pr,-tId))
            self.priorityHash[tId] = pr
            self.userHash[tId] = uId
        heapq.heapify(self.taskHeap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.userHash[taskId] = userId
        self.priorityHash[taskId] = priority
        heapq.heappush(self.taskHeap,(-priority,-taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.priorityHash[taskId] = newPriority
        heapq.heappush(self.taskHeap,(-newPriority,-taskId))

    def rmv(self, taskId: int) -> None:
        self.userHash[taskId] = -1

    def execTop(self) -> int:
        while self.taskHeap: 
            pr, tId = heapq.heappop(self.taskHeap)
            pr, tId = -pr, -tId
            if self.priorityHash[tId] == pr and self.userHash[tId] != -1:
                ans = self.userHash[tId]
                self.userHash[tId] = -1
                return ans
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()